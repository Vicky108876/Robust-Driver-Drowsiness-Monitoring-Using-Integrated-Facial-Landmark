# Robust-Driver-Drowsiness-Monitoring-Using-Integrated-Facial-Landmark
A real-time driver drowsiness detection system using MediaPipe Face Mesh, EAR, MAR, and MLP classifier to identify fatigue behaviors like microsleep and yawning, with instant alert system.
# Driver Drowsiness Detection System

Driver Drowsiness Detection System is an AI-powered real-time monitoring software that detects driver fatigue using integrated facial landmark analysis. The system combines MediaPipe Face Mesh, geometric feature extraction (EAR, MAR, Head Pose), and an optimized Multi-Layer Perceptron (MLP) classifier to identify drowsiness-related behaviors such as microsleep, yawning, and abnormal head movement.

---

## 📦 Download Dataset

You can download the dataset here:

👉 https://www.kaggle.com/datasets/matjazmuc/frame-level-driver-drowsiness-detection-fl3d

Dataset Name:  
**Frame Level Driver Drowsiness Detection and Alert Using Pygame**

---

## 🚗 About the Project

This project provides a GUI-based real-time driver monitoring pipeline for automated fatigue detection.

The complete workflow includes:

**Load Camera Feed → Facial Landmark Detection → Feature Extraction → Classification → Alert Generation**

The system is lightweight, non-intrusive, and suitable for real-time deployment.

---

## 🖼️ Live Camera Input

The system captures live video feed from the webcam.

The captured frames are continuously processed for driver monitoring.

<img width="932" height="511" alt="image" src="https://github.com/user-attachments/assets/861eb8da-4b69-469b-8652-54c8cbf84048" />

Live Driver Face Detection

---

## 📥 Facial Landmark Detection

MediaPipe Face Mesh detects **468 facial landmarks** from each frame.

This enables accurate tracking of:

- Eye landmarks
- Mouth landmarks
- Head pose coordinates

**Output:**  
Detected Facial Mesh Overlay

---

## 🎯 Feature Extraction

The extracted landmarks are used to compute:

### Eye Aspect Ratio (EAR)
Detects prolonged eye closure and microsleep.

### Mouth Aspect Ratio (MAR)
Detects yawning behavior.

### Head Pose Estimation
Tracks abnormal head movement.

**Output:**  
Real-time feature values

---

## 📊 Feature Processing

Extracted features undergo preprocessing:

- Data cleaning
- Label encoding
- Feature normalization

This improves classification accuracy.

**Output:**  
Optimized feature vector

---

## 🧠 Driver State Classification

The processed features are passed to the MLP classifier.

The classifier predicts driver state as:

- Alert
- Microsleep
- Yawning

**Example Output:**  
Classified as: **Microsleep**  
Confidence: **86%**

---

## 🔔 Alert Generation

If drowsiness is detected:

- Audio alert is triggered instantly
- Driver is warned in real-time

**Output:**  
Drowsiness Alert Activated

---

## 📈 Performance

### Model Accuracy
**86%**

### Detection Performance

- Alert Detection: High Accuracy
- Yawning Detection: Excellent
- Microsleep Detection: Moderate

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Scikit-learn
- Pygame

---

## 🖥️ System Workflow

These stages demonstrate the complete workflow:

**1. Capture Live Frame**  
**2. Detect Facial Landmarks**  
**3. Extract EAR / MAR / Head Pose**  
**4. Preprocess Features**  
**5. Classify Driver State**  
**6. Trigger Alert**

Each step is executed automatically with real-time feedback.

---

## 🚀 Future Enhancements

- Mobile app alert integration
- Cloud monitoring
- Night vision support
- Improved microsleep detection
- IoT vehicle integration

---

## 👨‍💻 Author

**Vignesh M**  
MCA  
SRM Arts and Science College

---

## 📜 License

This project is developed for academic and research purposes.
