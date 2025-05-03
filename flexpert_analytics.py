import streamlit as st
import json
import sqlite3
import pandas as pd
import plotly.express as px
import datetime
import requests
import os
from dotenv import load_dotenv

class FitnessDashboard:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        self.exercise_log_path = "./database/exercise_log.json"
        self.user_data_path = "./database/user_data.json"
        self.meal_plan_log_path = "./database/meal_plan_log.json"
        self.db_path = "./database/user_exercises.db"

    def load_json_data(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return []

    def load_sqlite_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM exercise_log", conn)
        conn.close()
        return df

    def save_meal_plan_log(self, meal_plan, fitness_goal):
        new_entry = {
            "date": str(datetime.date.today()),
            "fitness_goal": fitness_goal,
            "meal_plan": meal_plan
        }
        data = self.load_json_data(self.meal_plan_log_path)
        data.append(new_entry)
        with open(self.meal_plan_log_path, "w") as f:
            json.dump(data, f, indent=4)

    def fetch_meal_plan(self, detected_foods, fitness_goal):
        query = f"Generate a meal plan for a person focusing on {fitness_goal} with these ingredients: {', '.join(detected_foods)}."
        data = {"contents": [{"parts": [{"text": query}]}]}
        response = requests.post(f"{self.api_url}?key={self.api_key}", json=data)
        if response.status_code == 200:
            meal_plan = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            self.save_meal_plan_log(meal_plan, fitness_goal)
            return meal_plan
        return "❌ Error generating meal plan."

    def run(self):
        st.header("📊 Your Fitness Journey with Flexpert")
        st.write("Track your **progress** and stay motivated! 📈")

        # Load data
        dashboard = FitnessDashboard()
        exercise_log = dashboard.load_json_data("./database/exercise_log.json")
        user_data = dashboard.load_json_data("./database/user_data.json")
        exercise_df = self.load_sqlite_data()

        # Extract user details
        fitness_goal = user_data.get("goal", "Maintain")
        detected_foods = [log.get("exercise_name", "Unknown") for log in exercise_log]

        # Generate meal plan
        meal_plan = self.fetch_meal_plan(detected_foods, fitness_goal)

        # Display meal plan
        st.subheader("🍽 Customized Meal Plan")
        st.write(meal_plan)

        # Visualizations
        st.subheader("📊 Workout Performance")
        if not exercise_df.empty:
            fig = px.bar(exercise_df, x="exercise_name", y="calories", color="exercise_name", title="Calories Burned by Exercise")
            st.plotly_chart(fig)

            fig2 = px.line(exercise_df, x="exercise_name", y="score", color="exercise_name", title="Workout Form Scores Over Time")
            st.plotly_chart(fig2)
        else:
            st.info("No exercise data available yet.")

        st.sidebar.info("💡 Stay consistent! Track your workouts and diet to maximize results.")


