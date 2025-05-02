import mediapipe as mp
import cv2
import numpy as np
import math
import time
import sys
import sqlite3
import matplotlib.pyplot as plt
import json

class AITrainer:
    def __init__(self, exercise_name, rep_count):
        self.exercise_name = exercise_name
        self.rep_count = rep_count
        self.score_list = []
        self.count = 0
        self.dir = 0
        self.cap = cv2.VideoCapture(0)
        self.pose = mp.solutions.pose.Pose()
        self._init_db()

    def _init_db(self):
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

    def find_angle(self, img, lmList, p1, p2, p3, draw=True):
        x1, y1 = lmList[p1][1:]
        x2, y2 = lmList[p2][1:]
        x3, y3 = lmList[p3][1:]
        
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
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

    # Define exercise landmark mappings and calorie burn per rep
    WORKOUTS = {
        "Bicep Curls": (11, 13, 15),  # Shoulder, Elbow, Wrist
        "Squats": (24, 26, 28),       # Hip, Knee, Ankle
        "Push-ups": (12, 14, 16),     # Shoulder, Elbow, Wrist
        "Lunges": (24, 26, 28),       # Hip, Knee, Ankle
        "Deadlifts": (24, 26, 28),    # Hip, Knee, Ankle
        "Planks": (12, 14, 16),       # Shoulder, Elbow, Wrist
        "Bench Press": (12, 14, 16)   # Shoulder, Elbow, Wrist
    }

    CALORIES_PER_REP = {
        "Bicep Curls": 0.5,
        "Squats": 0.8,
        "Push-ups": 0.7,
        "Lunges": 0.6,
        "Deadlifts": 1.2,
        "Planks": 0.3,
        "Bench Press": 1.0
    }

    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    pTime = 0
    dir = 0
    count = 0
    cap = cv2.VideoCapture(0)

    # Timer for exercise duration
    exercise_duration = rep_count * 8  # Each rep is 10 seconds
    start_time = time.time()
    end_time = time.time() + exercise_duration
    score_list = []

    print(time.time())
    print(start_time)
    print(end_time)

# --- Main Script Execution ---
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Please provide an exercise name and rep count.")
        sys.exit(1)

    exercise_name = sys.argv[1]
    rep_count = int(sys.argv[2])

    trainer = AITrainer(exercise_name, rep_count)
    trainer.start_session()
