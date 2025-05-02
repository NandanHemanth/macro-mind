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