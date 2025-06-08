# 🧠 StudyBuzz – Real-Time Drowsiness and Yawning Detection System

StudyBuzz is a real-time computer vision tool that monitors eye and mouth movements to detect signs of drowsiness and yawning using your webcam. Designed with students in mind, it provides instant voice alerts to help you stay focused while studying.

## 🔍 Features

- 👁️ Detects **eye closure** using Eye Aspect Ratio (EAR)
- 😮 Detects **yawning** using Mouth Aspect Ratio (MAR)
- 🔊 Real-time **text-to-speech alerts**
- 🧠 Works entirely **offline** using `pyttsx3`
- ⏳ Includes a **cooldown timer** to avoid repeated alerts
- ⚙️ Built with `MediaPipe`, `OpenCV`, and `Python`

## 📸 How It Works

Webcam Input → MediaPipe FaceMesh → EAR & MAR Calculation → Condition Check → Text-to-Speech Alert

- EAR < 0.25 (for 2 seconds) → "Eyes closed! Wake up!"
- MAR > 0.03 → "You are yawning. Stay awake!"

## 🛠️ Installation

1. Clone the repo
	git clone https://github.com/your-username/StudyBuzz.git
2. (Optional) Create a virtual environment	
	python -m venv venv
	source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
	pip install -r requirements.txt

## 🚀 Usage
	python main.py

Make sure your webcam is active.

Keep your face visible in the camera.

Press q to exit.

## 🧪 Requirements
opencv-python
mediapipe
pyttsx3

## 📂 Project Structure
StudyBuzz/
├── main.py                  # Main application script
├── requirements.txt         # Required packages
├── README.md                # GitHub readme
├── StudyBuzz_Report.pdf     # Summary report 
├── StudyBuzz_Presentation.pptx  # Presentation slides
└── demo_video.mp4           # video demo

## 🔮 Future Enhancements

- Session logging & analytics
- User calibration for EAR/MAR thresholds
- Browser integration (Chrome/Zoom)
- Mobile version with offline speech alerts

## 👩‍💻 Author
Roopakjeet Kaur
Developed as part of the ELC Computer Vision Activity at Thapar Institute of Engineering and Technology (2024–25)

## 📄 License
This  project is licensed under the MIT License.


