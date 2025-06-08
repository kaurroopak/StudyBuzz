StudyBuzz - Real-Time Drowsiness and Yawning Detection System

Project Title: StudyBuzz - Stay Awake, Stay Sharp!

Objective:
StudyBuzz is a real-time computer vision application that monitors students while studying using a webcam. It detects signs of drowsiness (eye closure) and yawning and provides instant voice alerts to help the user stay focused and awake.


Key Features:

1. Real-time webcam monitoring using OpenCV and MediaPipe.
2. Eye Aspect Ratio (EAR) based drowsiness detection.
3. Mouth Aspect Ratio (MAR) based yawning detection.
4. Voice-based alerts using pyttsx3 (Text-to-Speech).
5. Cooldown mechanism to avoid repeating alerts too frequently.


Technologies Used:

Python 3.7+ , OpenCV , MediaPipe , pyttsx3 (offline TTS) , Math , Time , Threading modules


Dataset:
This project does not use an external dataset. It works on real-time webcam input using MediaPipe FaceMesh which is pretrained for facial landmark detection.


Installation Instructions:

1. Clone or download this repository.

2. (Optional but recommended) Create a virtual environment:

	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies:

	pip install -r requirements.txt


How to Run the Code:

1. Open a terminal in the project directory.

2. Run the following command:

	python main.py

3. Keep your face visible in the webcam frame.

4. Voice alerts will trigger when:

	Eyes are closed for more than 2 seconds.

	A yawn is detected.

5. Press q to exit the application.


File Structure:

StudyBuzzR/
├── main.py              	  # Main application file
├── README.txt           	  # Instructions and project summary
├── requirements.txt     	  # Dependency list
├── StudyBuzzR_Report.pdf 	  # Summary report (for submission)
├── StudyBuzzR_Presentation.pptx  # Presentation (if applicable)
└── demo_video.mp4       	  # Optional demo video


Voice Alerts:

"Eyes closed! Wake up!"

"You are yawning. Stay awake!"


Acknowledgments:
Developed as part of the ELC Computer Vision Activity (2024-25) at Thapar Institute of Engineering and Technology during 4th semester.

