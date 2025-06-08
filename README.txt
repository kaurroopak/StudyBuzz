🧠 StudyBuzz – Real-Time Drowsiness and Yawning Detection System

StudyBuzz is a real-time computer vision tool that monitors eye and mouth movements to detect signs of drowsiness and yawning using your webcam. Designed with students in mind, it provides instant voice alerts to help you stay focused while studying.


🔍 Features

- 👁️ Detects **eye closure** using Eye Aspect Ratio (EAR)
- 😮 Detects **yawning** using Mouth Aspect Ratio (MAR)
- 🔊 Real-time **text-to-speech alerts**
- 🧠 Works entirely **offline** using `pyttsx3`
- ⏳ Includes a **cooldown timer** to avoid repeated alerts
- ⚙️ Built with `MediaPipe`, `OpenCV`, and `Python`


📸 How It Works

Webcam Input → MediaPipe FaceMesh → EAR & MAR Calculation → Condition Check → Text-to-Speech Alert

- EAR < 0.25 (for 2 seconds) → "Eyes closed! Wake up!"
- MAR > 0.03 → "You are yawning. Stay awake!"


🛠️ Installation

1. Clone the repository
2. (Optional) Create a virtual environment	
	python -m venv venv
	source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
	pip install -r requirements.txt

🚀 How to Run the code: 

1. Open a terminal in the project directory.
2. Run the following command:
	python main.py
3. Keep your face visible in the webcam frame.
4. Voice alerts will trigger when:
	"Eyes are closed for more than 2 seconds."
	"A yawn is detected."
5. Press q to exit the application.


🧪 Requirements
opencv-python
mediapipe
pyttsx3


📂 Project Structure

StudyBuzz/
├── StudyBuzzz_main.py            # Main application file
├── README.txt           	  # Instructions and project summary
├── requirements.txt     	  # Dependency list
├── StudyBuzzR_Report.pdf 	  # Summary report 
├── StudyBuzzR_Presentation.pptx  # Presentation 
└── demo_video.mp4       	  # Demo video


🗣️ Voice Alerts:

"Eyes closed! Wake up!"
"You are yawning. Stay awake!"


🔮 Future Enhancements

- Session logging & analytics
- User calibration for EAR/MAR thresholds
- Browser integration (Chrome/Zoom)
- Mobile version with offline speech alerts


👩‍💻 Author
Roopakjeet Kaur
Developed as part of the ELC Computer Vision Activity at Thapar Institute of Engineering and Technology (2024–25)


📄 License
This  project is licensed under the MIT License.
