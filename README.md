# 💪 MacroMind – Your Personal AI Fitness and Nutrition Hub

An intelligent lifestyle assistant built using Streamlit that brings together personalized fitness, smart grocery planning, and AI-powered nutrition insights.

---

## 🚀 Getting Started

Follow the steps below to set up and run the MacroMind application:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/macro-mind.git
```

### 2. Navigate to the Project Directory
```bash
cd macro-mind
```

### 3. Create a `.env` File in the Current Directory

### 4. Add the Following Line and Save the File
```bash
GEMINI_API_KEY='AIzaSyBURHGqOsIdkmD8SWVmy0K7SUvApoDZel4'
```

> ⚠️ Make sure to replace the API key with your own if needed.

### 5. Install All Required Python Packages
```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`. Here's a snapshot:

```text
mediapipe
opencv-python
numpy
streamlit
streamlit-lottie
requests
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
pandas
matplotlib
plotly
pyzbar
python-dotenv
openai
pytesseract
ultralytics
torch
torchvision
torchaudio
```

---

## 🧪 Demo Instructions (Step-by-Step)

After launching the app using `streamlit run app.py`, follow these steps to experience the full workflow:

### 1. Create Your Profile
- Navigate to the **Profile** section.
- Enter your name, height, weight, goal, and dietary restrictions.
- Click **Save Profile**.

### 2. Start a Training Session
- Go to **Cbuminator**.
- Select **"Bicep Curls"** as the exercise.
- Choose the number of reps using the slider.
- Click **Start Training** to get form scores and calories burned.

### 3. Upload a Food Image
- Go to **Keto-Kat**.
- Upload an image of a refrigerator with food (available in the `macro-mind` repo or use your own image).
- The app will recognize foods, show nutrition stats, and suggest a meal plan based on your inputs.

### 4. Generate a Personalized Diet Plan
- Navigate to **Flexpert**.
- Click **Generate Plan**.
- The app will create a daily diet plan and display performance analytics.

### 5. Get Smart Grocery Recommendations
- Visit the **Shopping** section.
- You will see shopping links automatically generated from your meal plan.

> ⚠️ Please follow each step in order to unlock the complete experience and results!

## 👥 Team Members

- Nandan Hemanth  
- Nawaz Fateen Khan  
- Murali Sai Buddakkagari Venkata

---

🛠 Built with ❤️ using Python, Streamlit, and Gemini API.
