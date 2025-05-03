import streamlit as st
import json
import os
import requests
import pandas as pd
from dotenv import load_dotenv

class GroceryChecklist:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        self.meal_plan_log_path = "./database/meal_plan_log.json"

    def load_meal_plan_log(self):
        """Load past meal plans."""
        if os.path.exists(self.meal_plan_log_path):
            with open(self.meal_plan_log_path, "r") as file:
                return json.load(file)
        return []

    def generate_grocery_list(self, meal_plan):
        """Generate a categorized grocery list from the meal plan using Gemini AI."""
        query = f"Extract and categorize ingredients from this meal plan into a structured grocery shopping list: {meal_plan}."
        data = {"contents": [{"parts": [{"text": query}]}]}
        response = requests.post(f"{self.api_url}?key={self.api_key}", json=data)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return "❌ Error generating grocery list."

    def create_grocery_table(self, grocery_list):
        """Convert the raw list into a DataFrame with Walmart shopping links."""
        items = grocery_list.split("\n")
        grocery_data = {"Item": [], "Walmart Link": []}

        for item in items:
            item_name = item.strip()
            if item_name:
                walmart_url = f"https://www.walmart.com/search?q={item_name.replace(' ', '+')}"
                grocery_data["Item"].append(item_name)
                grocery_data["Walmart Link"].append(walmart_url)

        return pd.DataFrame(grocery_data)

    def run(self):
        st.header("🛒 AI-Generated Grocery Checklist")
        st.write("Automatically extracted from your **meal plans**!")

        meal_plan_log = self.load_meal_plan_log()
        if not meal_plan_log:
            st.warning("⚠ No meal plans found! Generate a meal plan first.")
            return

        latest_meal_plan = meal_plan_log[-1]["meal_plan"]
        grocery_list = self.generate_grocery_list(latest_meal_plan)

        if grocery_list.startswith("❌"):
            st.error(grocery_list)
            return

        grocery_df = self.create_grocery_table(grocery_list)
        st.write("📝 **Your Grocery List**")
        st.dataframe(grocery_df, width=800)

        # Checkboxes for shopping progress
        checked_items = []
        for _, row in grocery_df.iterrows():
            checked = st.checkbox(f"{row['Item']}", key=row['Item'])
            if checked:
                checked_items.append(row['Item'])

        st.write(f"✅ {len(checked_items)} / {len(grocery_df)} items checked")

        st.write("🛍 **Click below to shop on Walmart:**")
        for _, row in grocery_df.iterrows():
            st.markdown(f"🔗 [Shop for **{row['Item']}**]({row['Walmart Link']})")

        st.sidebar.info("💡 AI-powered shopping helps you stay on track with your health goals!")
