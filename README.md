# MacroMind: AI-Powered Lifestyle SuperApp 💪

**Team Members:**  
- Nandan Hemanth  
- Murali Sai  
- Nawaz Fateen Khan  

MacroMind is an intelligent fitness and nutrition companion that helps users track workouts, assess form, and manage dietary goals — all through an interactive Streamlit interface.

This SuperApp features real-time pose evaluation, form scoring via webcam using AI (MediaPipe), automated calorie estimation, and animated feedback. It also includes a user profile system and nutrition guidance modules.

---

## 🚀 Key Features

- **🏋️ Workout AI (Cbuminator)**  
  Real-time form analysis using webcam-based pose detection (via MediaPipe). Calculates:
  - Form score (frame-wise scoring and visualization)
  - Estimated calories burned
  - Repetition count

- **📈 Performance Chart**  
  After each workout session, the app auto-generates a score graph saved to `./database/form_score_chart.png` and displays it in the UI.

- **🧑 Profile Management**  
  Save and retrieve user details such as height, weight, fitness goals, and dietary restrictions.

- **🎨 Lottie Animations**  
  Custom animated feedback enhances user experience in the Streamlit sidebar and pages.

---

## 🔧 Prerequisites

Ensure Python 3.8+ is installed and the following libraries are available:

- `streamlit`
- `opencv-python`
- `mediapipe`
- `matplotlib`
- `pandas`
- `numpy`
- `pillow`
- `requests`
- `plotly`
- `streamlit-lottie`

---

## 📦 Installation & Setup

1. Clone this repository or download the project files:
   ```bash
   git clone https://github.com/NandanHemanth/macro-mind.git
   ```
2. Change into the Current working repository
   ```bash
   cd MacroMind
   ```

3. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application using Streamlit:
    ```bash
    streamlit run app.py
    ```