import os
import requests
import base64
import json
from dotenv import load_dotenv

class FoodAnalyzer:
    def __init__(self):
        """Initialize the FoodAnalyzer with API key and endpoint."""
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        self.database_path = "./database/meal_data.json"
        os.makedirs(os.path.dirname(self.database_path), exist_ok=True)

    def encode_image(self, image_path):
        """Encode image to Base64."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def recognize_food(self, image_path):
        """Recognize food items from an image."""
        image_base64 = self.encode_image(image_path)
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_base64}},
                    {"text": "List all food items present in this image."}
                ]
            }]
        }
        response = requests.post(f"{self.api_url}?key={self.api_key}", json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            foods = result["candidates"][0]["content"]["parts"][0]["text"]
            return foods.split(", ")
        return []

    def get_nutrition_facts(self, food_items):
        """Get nutrition facts for a list of foods."""
        query = f"Provide detailed nutrition facts for these food items: {', '.join(food_items)}."
        data = {"contents": [{"parts": [{"text": query}]}]}
        response = requests.post(f"{self.api_url}?key={self.api_key}", json=data)
        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        return "❌ Error fetching nutrition facts."

    def suggest_recipes(self, food_items):
        """Suggest recipes based on food items."""
        query = f"Suggest 3 recipes using these ingredients: {', '.join(food_items)}."
        data = {"contents": [{"parts": [{"text": query}]}]}
        response = requests.post(f"{self.api_url}?key={self.api_key}", json=data)
        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        return "❌ Error fetching recipes."

    def save_meal_data(self, detected_foods, nutrition_facts, meal_plan):
        """Save meal data to a JSON file."""
        entry = {
            "detected_foods": detected_foods,
            "nutrition_facts": nutrition_facts,
            "meal_plan": meal_plan
        }

        try:
            with open(self.database_path, "r") as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.append(entry)

        with open(self.database_path, "w") as file:
            json.dump(existing_data, file, indent=4)

        print("✅ Meal data saved successfully!")
