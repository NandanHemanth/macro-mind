# Macro-Mind : LifeStyle SuperApp
## Nandan Hemanth
## Murali Sai
## Nawaz Fateen Khan

This project provides a simple video recording application using Streamlit. It allows the user to start a 30-second video recording from the webcam and save it in a local directory (`./recording`). The recording functionality is encapsulated in a Python class, while the user interface is built with Streamlit.

## Features:
- **30-second video recording**: Records video for 30 seconds or until manually stopped.
- **Streamlit Interface**: Provides a simple and user-friendly web interface to start and stop recording.
- **Save Videos Locally**: Videos are saved in the `./recording` directory.
- **Basic Webcam Interaction**: Allows users to capture video using the webcam.

## Prerequisites:
Ensure you have Python installed. The project uses the following libraries:
- `streamlit`
- `opencv-python`

## Installation:

1. Clone the repository or download the project files.
2. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application using Streamlit:
    ```bash
    streamlit run app.py
    ```