# video_recorder.py

import cv2
import os
import time

class VideoRecorder:
    def __init__(self, duration=30, save_path='./recording'):
        """Initializes the video recorder with the specified duration and save path."""
        self.duration = duration
        self.save_path = save_path
        self.create_recording_folder()
        self.capture = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for video saving
        self.video_writer = None
        self.start_time = None

    def create_recording_folder(self):
        """Creates the recording folder if it doesn't exist."""
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def start_recording(self):
        """Starts recording video from the webcam and saves it to the specified path."""
        if not self.capture.isOpened():
            print("Error: Unable to access the camera.")
            return
        
        # Get video frame width and height
        frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create a VideoWriter object to save the video
        video_filename = os.path.join(self.save_path, f"recording_{int(time.time())}.avi")
        self.video_writer = cv2.VideoWriter(video_filename, self.fourcc, 20.0, (frame_width, frame_height))

        self.start_time = time.time()
        print("Recording started...")

        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break
            
            # Write the frame to the video file
            self.video_writer.write(frame)

            # Display the frame for live preview
            cv2.imshow("Recording...", frame)

            # Stop recording after 30 seconds
            if time.time() - self.start_time > self.duration:
                print("Recording finished.")
                break

            # Stop recording if the user presses the 'Esc' key
            if cv2.waitKey(1) & 0xFF == 27:  # 'Esc' key
                print("Recording stopped by user.")
                break

        # Release the video capture and writer
        self.capture.release()
        self.video_writer.release()
        cv2.destroyAllWindows()

