# app.py

import streamlit as st
from video_recorder import VideoRecorder

def main():
    st.title("🎥 Video Recorder")
    
    st.write("This is a basic video recorder app. You can start a 30-second recording and save it to the `./recording` folder.")
    
    if st.button("Start Recording"):
        st.write("Recording started... 🏃‍♂️")
        
        # Create an instance of VideoRecorder
        recorder = VideoRecorder(duration=30)
        
        # Start recording
        recorder.start_recording()
        
        st.success("Recording finished and saved successfully! 🎬")
        st.write("You can check the saved video in the `./recording` folder.")
    
    if st.button("Stop Recording"):
        st.write("Recording stopped manually. 🎬")

if __name__ == "__main__":
    main()
