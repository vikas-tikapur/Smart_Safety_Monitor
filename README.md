# 🛡️ Smart Safety Monitor

A real-time AI-powered safety monitoring system built using **Python**, **OpenCV**, and **YOLOv8**.

This project is designed to monitor workplace safety by detecting people, mobile phones, helmets, safety vests, and other safety-related objects in real time.

---

# Features

## Implemented

* Real-Time Webcam Monitoring
* YOLOv8 Object Detection
* Real-Time Person Detection
* Live Person Counter
* Mobile Phone Detection
* Live Mobile Phone Counter
* Color-Coded Bounding Boxes
* Modular Project Architecture
* Well-Documented Source Code

---

## Upcoming Features

* Automatic Screenshot Capture
* CSV Event Logging
* Helmet Detection
* Safety Vest Detection
* Weapon Detection
* Dashboard Analytics
* Detection Statistics
* Safety Alerts

---

# Project Structure

```text
Smart_Safety_Monitor/
│
├── dashboard/
├── logs/
├── models/
├── output/
├── screenshots/
│
├── utils/
│   ├── camera.py
│   ├── constants.py
│   ├── detector.py
│   ├── drawing.py
│   └── mobile_detector.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Tech Stack

* Python 3.10
* OpenCV
* YOLOv8 (Ultralytics)
* PyTorch
* NumPy

---

# How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vikas-tikapur/Smart_Safety_Monitor.git
cd Smart_Safety_Monitor
```

### 2. Create a virtual environment

```bash
py -3.10 -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

---

# Current Progress

| Feature                | Status |
| ---------------------- | ------ |
| Project Setup          | ✅      |
| Camera Module          | ✅      |
| YOLO Model Loader      | ✅      |
| Person Detection       | ✅      |
| Person Counter         | ✅      |
| Mobile Phone Detection | ✅      |
| Mobile Phone Counter   | ✅      |
| Screenshot Capture     | 🚧     |
| CSV Logging            | 🚧     |
| Helmet Detection       | 🚧     |
| Safety Vest Detection  | 🚧     |
| Weapon Detection       | 🚧     |
| Dashboard              | 🚧     |

---

# Project Goals

* Improve workplace safety using AI.
* Detect safety violations in real time.
* Generate event logs for monitoring.
* Capture screenshots of safety violations.
* Build a modular and maintainable computer vision project.

---

# Author

**Vikas Mishra**

GitHub:
https://github.com/vikas-tikapur
