# 🛡️ Smart Safety Monitor

A real-time **AI-powered Workplace Safety Monitoring System** built using **Python**, **OpenCV**, **YOLOv8**, and **Tkinter Dashboard**.

The application monitors live webcam footage and detects workplace safety violations such as **persons** and **mobile phones** using the YOLOv8 COCO model. It also integrates a dedicated **PPE Detection Model** for detecting **helmets**, **safety vests**, and **no-helmet violations**.

The system automatically captures screenshots, logs events into CSV files, and provides a professional real-time dashboard for monitoring workplace safety.

---

# Features

## Implemented

* Real-Time Webcam Monitoring
* YOLOv8 COCO Object Detection
* Real-Time Person Detection
* Live Person Counter
* Mobile Phone Detection
* Live Mobile Phone Counter
* Smart Screenshot Capture
* CSV Event Logging
* Live FPS Counter
* Professional Monitoring Status Panel
* Live Date & Time
* Color-Coded Bounding Boxes
* Tkinter Dashboard
* Dashboard Analytics
* Dashboard Refresh
* Latest Event Viewer
* Last Screenshot Viewer
* Dual YOLO Model Architecture
* PPE Model Integration
* Modular Project Architecture
* Well-Documented Source Code

---

# In Progress

* Helmet Detection Validation
* No Helmet Detection
* Safety Vest Detection
* PPE Bounding Boxes
* PPE Event Logging
* PPE Dashboard Statistics
* PPE Screenshot Capture

---

# Planned Features

* Weapon Detection
* Email Alerts
* Safety Violation Alerts
* Dashboard Charts
* Daily Reports
* RTSP Camera Support
* Multi-Camera Monitoring
* Video File Support
* Performance Optimization

---

# Project Structure

```text
Smart_Safety_Monitor/
│
├── dashboard/
│   ├── __init__.py
│   ├── analytics.py
│   └── dashboard.py
│
├── logs/
├── models/
│   ├── coco/
│   ├── ppe/
│   └── weapon/
│
├── output/
├── screenshots/
│
├── utils/
│   ├── camera.py
│   ├── constants.py
│   ├── date_time.py
│   ├── detector.py
│   ├── drawing.py
│   ├── fps.py
│   ├── logger.py
│   ├── mobile_detector.py
│   ├── ppe_detector.py
│   └── screenshot.py
│
├── main.py
├── test_ppe_model.py
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
* Pandas
* Tkinter

---

# Installation

## Clone Repository

```bash
git clone https://github.com/vikas-tikapur/Smart_Safety_Monitor.git

cd Smart_Safety_Monitor
```

## Create Virtual Environment

```bash
py -3.10 -m venv venv
```

## Activate Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run Application

## Start Smart Safety Monitor

```bash
python main.py
```

## Open Dashboard

```bash
python -m dashboard.dashboard
```

---

# AI Models

| Model        | Purpose                   | Status |
| ------------ | ------------------------- | :----: |
| YOLOv8 COCO  | Person & Mobile Detection |    ✅   |
| PPE Model    | Helmet, Vest & No Helmet  |   🚧   |
| Weapon Model | Gun & Knife Detection     |   🚧   |

---

# 📈 Current Progress

| Module                      | Status |
| --------------------------- | :----: |
| Project Architecture        |    ✅   |
| Camera Module               |    ✅   |
| Object Detection            |    ✅   |
| Person Detection            |    ✅   |
| Mobile Detection            |    ✅   |
| Screenshot Manager          |    ✅   |
| CSV Event Logging           |    ✅   |
| Dashboard UI                |    ✅   |
| Dashboard Analytics         |    ✅   |
| FPS Counter                 |    ✅   |
| Date & Time                 |    ✅   |
| Dual YOLO Architecture      |    ✅   |
| PPE Model Integration       |    ✅   |
| Helmet Detection Validation |   🚧   |
| Safety Vest Detection       |   🚧   |
| Weapon Detection            |   🚧   |

**Overall Project Completion:** **≈ 85%**

---

# Project Goals

* Improve workplace safety using AI.
* Detect safety violations in real time.
* Capture screenshots as evidence.
* Generate CSV event logs.
* Provide live monitoring dashboard.
* Support multiple AI detection models.
* Integrate custom YOLOv8 models.
* Support CCTV and RTSP cameras.

---

# Current Version

## **v0.5.0 — Dual YOLO Architecture & Dashboard**

### Completed

* Professional Modular Architecture
* Dual YOLO Model Support
* Person Detection
* Mobile Phone Detection
* Screenshot Capture
* CSV Event Logging
* Dashboard Analytics
* Live Dashboard Refresh
* FPS Counter
* Professional Monitoring Panel
* PPE Model Integration

### In Progress

* Helmet Detection Validation
* Safety Vest Detection
* No Helmet Detection
* Weapon Detection
* AI Alerts

---

# Author

**Vikas Mishra**

GitHub: https://github.com/vikas-tikapur

---

**If you found this project useful, consider giving it a star on GitHub!**
