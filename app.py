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
import matplotlib.pyplot as plt
import plotly.express as px



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
    def load_data(self):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                return (
                    data.get("name", ""),
                    data.get("height", 170),
                    data.get("weight", 70),
                    data.get("goal", ""),
                    data.get("dietary_restriction", "")
                )
        except:
            self.init_data()
            return ("", 170, 70, "", "")
        
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
        
        
class AITrainer:
    @staticmethod
    def run(exercise, reps):
        result = subprocess.run(
            ["python", "AI_God.py", exercise, str(reps)],
            capture_output=True,
            text=True
        )
        score, calories = None, None
        for line in result.stdout.split("\n"):
            if "Score:" in line and "Calories Burned:" in line:
                parts = line.split("|")
                try:
                    score = float(parts[0].split("Score:")[1].strip().replace("%", ""))
                    calories = float(parts[1].split("Calories Burned:")[1].strip())
                except:
                    pass
        return score, calories



class Nutritionist:
    def __init__(self):
        self.detected_foods = []

    def recognize_and_analyze(self, image_path):
        self.detected_foods = recognize_food(image_path)
        nutrition_facts = get_nutrition_facts(self.detected_foods)
        return self.detected_foods, nutrition_facts

    def get_macro_breakdown(self, nutrition_facts):
        macro_data = {"Calories": 0, "Proteins": 0, "Fats": 0, "Carbs": 0}
        for line in nutrition_facts.split("\n"):
            digits = "".join(filter(str.isdigit, line))
            if digits:
                value = int(digits)
                if "calories" in line.lower():
                    macro_data["Calories"] += value
                elif "protein" in line.lower():
                    macro_data["Proteins"] += value
                elif "fat" in line.lower():
                    macro_data["Fats"] += value
                elif "carb" in line.lower():
                    macro_data["Carbs"] += value
        return macro_data
    


profile_manager = UserProfileManager()
nutritionist = Nutritionist()


keto_kat_animation = LottieLoader.load('https://lottie.host/89ed7481-222e-4850-879d-a96471c32534/3hVtb56VQF.json')
cbuminator_animation = LottieLoader.load('https://lottie.host/0aa94491-176f-4cfd-a7a3-48fdc2cbc844/A3C89do9KL.json')
pet_animation = LottieLoader.load("https://lottie.host/27b7d9f3-211d-4ce8-b8a3-453d3e2c5439/0YWqdBtdv7.json")
shopping_animation = LottieLoader.load('https://lottie.host/bb02a444-4aa8-4fea-bd38-d46fae3b0baf/XDdL3IbPh7.json')

st.sidebar.title("🚀 MacroMind Menu")
page = st.sidebar.radio("Personal AI Hub", ["🏠 Profile", "🏋️ Cbuminator"])

with st.sidebar:
    st_lottie(pet_animation, height=200, key="keto_pet")


if page == "🏠 Profile":
    st.header("Your Profile")
    name, height, weight, goal, dietary_restriction = profile_manager.load_data()
    name = st.text_input("Name:", name)
    height = st.number_input("Height (cm):", min_value=100, max_value=250, value=height)
    weight = st.number_input("Weight (kg):", min_value=30, max_value=200, value=weight)
    goal = st.text_input("Fitness Goal:", goal)
    dietary_restriction = st.text_area("Dietary Restrictions:", dietary_restriction)
    if st.button("Save Profile"):
        profile_manager.save_data(name, height, weight, goal, dietary_restriction)
        st.success("Profile saved!")

elif page == "🏋️ Cbuminator":
    st.header("Meet Cbuminator")
    exercise = st.selectbox("Choose Exercise", ["Bicep Curls", "Squats", "Push-ups"])
    reps = st.slider("Reps", 2, 20)
    if st.button("Start Training"):
        score, calories = AITrainer.run(exercise, reps)
        if score is not None and calories is not None:
            st.success(f"Form Score: {score}%")
            st.success(f"Calories Burned: {calories} kcal")

            chart_path = "./database/form_score_chart.png"
            if os.path.exists(chart_path):
                st.image(chart_path, caption="Your Form Score Over Time", use_container_width=True)
            else:
                st.warning("Form score chart not found.")
        else:
            st.error("Could not evaluate performance")



st.markdown("""
<style>
.footer {
    bottom: 0;
    width: 100%;
    text-align: center;
    padding: 0px;
    font-size: 16px;
}
</style>
<div class='footer'>Made by MacroMind with ❤️</div>
""", unsafe_allow_html=True)



