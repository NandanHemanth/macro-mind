import mediapipe as mp
import cv2
import numpy as np


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