import mediapipe as mp
import cv2
import numpy as np
import math
import time
import sys
import sqlite3
import matplotlib.pyplot as plt
import os

class AITrainer:
    def __init__(self, exercise_name, rep_count):
        self.exercise_name = exercise_name
        self.rep_count = rep_count
        self.score_list = []
        self.count = 0
        self.dir = 0
        self.cap = cv2.VideoCapture(0)
        self.pose = mp.solutions.pose.Pose()
        self.pTime = 0
        self.start_time = time.time()
        self.end_time = self.start_time + rep_count * 8  # 8 sec per rep

        self.WORKOUTS = {
            "Bicep Curls": (11, 13, 15),
            "Squats": (24, 26, 28),
            "Push-ups": (12, 14, 16),
            "Lunges": (24, 26, 28),
            "Deadlifts": (24, 26, 28),
            "Planks": (12, 14, 16),
            "Bench Press": (12, 14, 16)
        }

        self.CALORIES_PER_REP = {
            "Bicep Curls": 0.5,
            "Squats": 0.8,
            "Push-ups": 0.7,
            "Lunges": 0.6,
            "Deadlifts": 1.2,
            "Planks": 0.3,
            "Bench Press": 1.0
        }

        self._init_db()

    def _init_db(self):
        os.makedirs("./database", exist_ok=True)
        conn = sqlite3.connect("./database/user_exercises.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS exercise_log (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            exercise_id INTEGER,
                            exercise_name TEXT,
                            reps INTEGER,
                            score REAL,
                            calories REAL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    def _log_exercise(self, reps, score, calories):
        conn = sqlite3.connect("./database/user_exercises.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO exercise_log (exercise_id, exercise_name, reps, score, calories) VALUES (?, ?, ?, ?, ?)",
                       (100, self.exercise_name, reps, score, calories))
        conn.commit()
        conn.close()

    def _find_angle(self, img, lmList, p1, p2, p3, draw=True):
        x1, y1 = lmList[p1][1:]
        x2, y2 = lmList[p2][1:]
        x3, y3 = lmList[p3][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle

    def start_session(self):
        mpDraw = mp.solutions.drawing_utils

        print(time.time())
        print(self.start_time)
        print(self.end_time)

        if not self.cap.isOpened():
            print("❌ Webcam could not be accessed.")
            return

        while time.time() < self.end_time:
            success, img = self.cap.read()
            if not success:
                break

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.pose.process(imgRGB)

            lmList = []
            if results.pose_landmarks:
                mpDraw.draw_landmarks(img, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                if len(lmList) != 0 and self.exercise_name in self.WORKOUTS:
                    p1, p2, p3 = self.WORKOUTS[self.exercise_name]
                    angle = self._find_angle(img, lmList, p1, p2, p3)
                    per = np.interp(angle, (60, 160), (100, 0))
                    self.score_list.append(per)

                    if per == 100 and self.dir == 0:
                        self.count += 0.5
                        self.dir = 1
                    if per == 0 and self.dir == 1:
                        self.count += 0.5
                        self.dir = 0

                    cv2.putText(img, str(self.count), (500, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            cTime = time.time()
            fps = 1 / (cTime - self.pTime) if cTime != self.pTime else 0
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.putText(img, "Time Left: " + str(int(self.end_time - time.time())),
                        (70, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Workout Tracker", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        self._end_session()

    def _end_session(self):
        average_score = sum(self.score_list) / len(self.score_list) if self.score_list else 0
        calories_burned = self.CALORIES_PER_REP.get(self.exercise_name, 0) * int(self.count)
        self._log_exercise(int(self.count), average_score, calories_burned)

        plt.plot(self.score_list, label="Form Score")
        plt.axhline(y=100, color='r', linestyle='--', label="CBum's Form")
        plt.xlabel("Frames")
        plt.ylabel("Score (%)")
        plt.title(f"{self.exercise_name} Form Score Comparison")
        plt.legend()
        plt.savefig("./database/form_score_chart.png")

        print(f"Workout {self.exercise_name} completed with {int(self.count)} reps! "
              f"Score: {average_score:.2f}% | Calories Burned: {calories_burned:.2f}")
        print("./database/form_score_chart.png")


# --- Main Execution ---
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Please provide an exercise name and rep count.")
        sys.exit(1)

    exercise_name = sys.argv[1]
    rep_count = int(sys.argv[2])
    trainer = AITrainer(exercise_name, rep_count)
    trainer.start_session()
