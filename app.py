import streamlit as st

# Set page configuration
st.set_page_config(page_title="MacroMind", page_icon="💪", layout="wide")

import requests
import json
import os
import subprocess
import sqlite3
from streamlit_lottie import st_lottie
from PIL import Image

class UserProfileManager:
    def __init__(self, path="./database/user_data.json"):
        self.path = path
        self.default_data = {
            "name": "",
            "height": 170,
            "weight": 70,
            "goal": "",
            "dietary_restriction": ""
        }
        self.init_data()
    
    def init_data(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self.save_data(**self.default_data)

    def save_data(self, name, height, weight, goal, dietary_restriction):
        data = {
            "name": name,
            "height": height,
            "weight": weight,
            "goal": goal,
            "dietary_restriction": dietary_restriction
        }
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
        



class LottieLoader:
    @staticmethod
    def load(url):
        try:
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        except:
            return None
        

class Nutritionist:
    def __init__(self):
        self.detected_foods = []

    def recognize_and_analyze(self, image_path):
        self.detected_foods = recognize_food(image_path)
        nutrition_facts = get_nutrition_facts(self.detected_foods)
        return self.detected_foods, nutrition_facts
