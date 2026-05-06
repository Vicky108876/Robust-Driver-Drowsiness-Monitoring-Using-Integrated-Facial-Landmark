# Robust-Driver-Drowsiness-Monitoring-Using-Integrated-Facial-Landmark
A real-time driver drowsiness detection system using MediaPipe Face Mesh, EAR, MAR, Head Pose and MLP classifier to identify fatigue behaviors like microsleep and yawning, with instant alert system.
# Driver Drowsiness Detection System

Driver Drowsiness Detection System is an AI-powered real-time monitoring software that detects driver fatigue using integrated facial landmark analysis. The system combines MediaPipe Face Mesh, geometric feature extraction (EAR, MAR, Head Pose), and an optimized Multi-Layer Perceptron (MLP) classifier to identify drowsiness-related behaviors such as microsleep, yawning, and abnormal head movement.

---

## 📦 Download Dataset

You can download the dataset here:

👉 https://drive.google.com/drive/folders/13kGo1QaYPAbude5fUyJ8DQuy1fN-QTF_?usp=drive_link

Dataset Name:  
**Frame Level Driver Drowsiness Detection (FL3D)**


## 🚗 About the Project

This project provides a GUI-based real-time driver monitoring pipeline for automated fatigue detection.

The complete workflow includes:

**Load Camera Feed → Facial Landmark Detection → Feature Extraction → Classification → Alert Generation**

The system is lightweight, non-intrusive, and suitable for real-time deployment.


## 1. 🖼️ Live Camera Input

The system captures live video feed from the webcam.

The captured frames are continuously processed for driver monitoring.

<img width="1283" height="488" alt="image" src="https://github.com/user-attachments/assets/a16b3e45-ad44-425a-aab3-77224a2b3180" />


Live Driver Face Detection

## 2. 📥 Facial Landmark Detection

MediaPipe Face Mesh detects **468 facial landmarks** from each frame.

This enables accurate tracking of:

- Eye landmarks
- Mouth landmarks
- Head pose coordinates

<img width="826" height="551" alt="image" src="https://github.com/user-attachments/assets/1e3fa26b-5b22-4919-ae41-43467bc4e160" />

Detected Facial Mesh Overlay

## 3. 🎯 Feature Extraction

The extracted landmarks are used to compute:

### Eye Aspect Ratio (EAR)
Detects prolonged eye closure and microsleep.

### Mouth Aspect Ratio (MAR)
Detects yawning behavior.

### Head Pose Estimation
Tracks abnormal head movement.


<img width="241" height="289" alt="image" src="https://github.com/user-attachments/assets/f80c522f-64a7-4cd8-87b7-8edbc22da90f" />

Real-time feature values

---

## 4. 📊 Feature Processing

Extracted features undergo preprocessing:

- Data cleaning
- Label encoding
- Feature normalization

This improves classification accuracy.

---

## 5. 🧠 Driver State Classification

The processed features are passed to the MLP classifier.

The classifier predicts driver state as:

- Alert
- Microsleep
- Yawning
  
# 1. Alert
<img width="1100" height="606" alt="image" src="https://github.com/user-attachments/assets/9c58b22f-7a4b-4f10-aa41-f8d4b47d11b7" />

# 2. Microsleep
<img width="1245" height="686" alt="image" src="https://github.com/user-attachments/assets/e945009d-da99-4f4f-b1a5-1292ac23224f" />

# 3. Yawning:
<img width="1283" height="686" alt="image" src="https://github.com/user-attachments/assets/a86f9abb-ae51-4841-9cf9-2a5851d43c22" />

# 5. Look right:
<img width="940" height="480" alt="report_20260507_005357" src="https://github.com/user-attachments/assets/aafa7c25-74be-4c3b-a8f6-d831d846982d" />

# 6. Look Left:
<img width="940" height="480" alt="report_20260507_005354" src="https://github.com/user-attachments/assets/99c5b684-6cfb-4745-84ac-d8c881c026c5" />

# 7. Look Up:
<img width="940" height="480" alt="report_20260507_005407" src="https://github.com/user-attachments/assets/ce36c394-3457-43aa-b129-6744182f22dc" />

# 8. Look Down:
<img width="940" height="480" alt="report_20260507_005402" src="https://github.com/user-attachments/assets/0ca878d2-d778-4238-a9d6-728a3185e40a" />

---

## 6. 🔔 Alert Generation

If drowsiness is detected:

- Audio alert is triggered instantly
- Driver is warned in real-time

<img width="1245" height="686" alt="image" src="https://github.com/user-attachments/assets/86d8db14-3f17-4531-9ef1-cfc2d4830731" />

Drowsiness Alert Activated


