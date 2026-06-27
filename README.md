# 🛡️ Smart Safety Monitor

A real-time **AI-powered Workplace Safety Monitoring System** built using **Python**, **OpenCV**, **YOLOv8**, and **Tkinter Dashboard**.

The application monitors live webcam footage and detects workplace safety violations using multiple AI models. It currently supports **Person Detection**, **Mobile Phone Detection**, **Helmet Detection**, **No Helmet Detection**, and **Safety Vest Detection**.

The system automatically captures screenshots, logs detection events into CSV files, and provides a professional real-time monitoring dashboard.

---

# Features

## Implemented

* Real-Time Webcam Monitoring
* YOLOv8 COCO Object Detection
* Real-Time Person Detection
* Live Person Counter
* Mobile Phone Detection
* Live Mobile Phone Counter
* PPE Detection
* Helmet Detection
* No Helmet Detection
* Safety Vest Detection
* Live PPE Counters
* Color-Coded Bounding Boxes
* Smart Screenshot Capture
* CSV Event Logging
* Live FPS Counter
* Professional Monitoring Status Panel
* Live Date & Time
* Tkinter Dashboard
* Dashboard Analytics
* Dashboard Refresh
* Latest Event Viewer
* Last Screenshot Viewer
* Dual YOLO Model Architecture
* Modular Project Architecture
* Well-Documented Source Code

---

# In Progress

* PPE Violation Logging
* PPE Dashboard Analytics
* Auto Dashboard Refresh
* Weapon Detection Integration
* Safety Alert System
* Violation Manager
* Performance Optimization

---

# Planned Features

* Weapon Detection
* Email Alerts
* Audio Alarm
* Dashboard Charts
* Daily Reports
* RTSP Camera Support
* Multi-Camera Monitoring
* Video File Processing
* AI-Based Safety Reports

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
├── videos/
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
├── test_ppe_video.py
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

---

## Create Virtual Environment

```bash
py -3.10 -m venv venv
```

---

## Activate Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

## Start Smart Safety Monitor

```bash
python main.py
```

---

## Open Dashboard

```bash
python -m dashboard.dashboard
```

---

# AI Models

| Model         | Purpose                                   | Status |
| ------------- | ----------------------------------------- | :----: |
| YOLOv8 COCO   | Person & Mobile Detection                 |    ✅   |
| PPE YOLOv8    | Helmet, No Helmet & Safety Vest Detection |    ✅   |
| Weapon YOLOv8 | Weapon Detection                          |   🚧   |

---

# Current Progress

| Module                | Status |
| --------------------- | :----: |
| Project Architecture  |    ✅   |
| Camera Module         |    ✅   |
| YOLOv8 COCO Detection |    ✅   |
| Person Detection      |    ✅   |
| Mobile Detection      |    ✅   |
| PPE Model Integration |    ✅   |
| Helmet Detection      |    ✅   |
| No Helmet Detection   |    ✅   |
| Safety Vest Detection |    ✅   |
| PPE Visualization     |    ✅   |
| Live PPE Counters     |    ✅   |
| Screenshot Manager    |    ✅   |
| CSV Event Logging     |    ✅   |
| Dashboard UI          |    ✅   |
| Dashboard Analytics   |    ✅   |
| FPS Counter           |    ✅   |
| Date & Time           |    ✅   |
| Weapon Detection      |   🚧   |
| AI Alerts             |   🚧   |
| RTSP Camera Support   |   🚧   |

### Overall Project Completion

**≈ 90%**

---

# Project Goals

* Improve workplace safety using AI.
* Detect workplace safety violations in real time.
* Capture screenshots as evidence.
* Generate CSV event logs.
* Provide live monitoring dashboard.
* Support multiple AI detection models.
* Integrate custom YOLOv8 models.
* Support CCTV and RTSP cameras.
* Build a scalable and maintainable Computer Vision application.

---

# System Architecture

```text
                    Webcam
                       │
                       ▼
                 Video Frame
                       │
      ┌────────────────┴────────────────┐
      ▼                                 ▼
YOLOv8 COCO Model                 PPE YOLO Model
(Person, Mobile)          (Helmet, No Helmet, Vest)
      │                                 │
      └────────────────┬────────────────┘
                       ▼
                 Drawing Module
                       │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Status Panel    Screenshot      Event Logger
                       │
                       ▼
                 Dashboard Analytics
```

---

# Screenshots

### Live Monitoring

>  ![Live Monitoring]!(live_detection.png)
![Live Monitoring] docs/images/live_detection_site.png

### Dashboard

> ![dashboard]!(dashboard.png)

### PPE Detection

> ![ppe detection]!(image-2.png)
!(image-4.png)

### No Helmet Detection
![No Helmet]screenshots/no_helmet_detected_2026-06-27_17-38-36-527989.jpg

---

# Current Version

## **v0.6.0 — PPE Detection & Live Monitoring**

### Completed

* Professional Modular Architecture
* Dual YOLO Model Pipeline
* Person Detection
* Mobile Phone Detection
* PPE Detection
* Helmet Detection
* No Helmet Detection
* Safety Vest Detection
* Live PPE Counters
* Professional Monitoring Panel
* Screenshot Capture
* CSV Event Logging
* Dashboard Analytics
* Live Dashboard Refresh
* FPS Counter
* Date & Time Display

### 🚧 In Progress

* PPE Violation Logging
* Violation Manager
* Weapon Detection
* AI Alerts
* RTSP Camera Support

---

# Author

**Vikas Mishra**

GitHub: https://github.com/vikas-tikapur

---

⭐ **If you found this project useful, consider giving it a Star on GitHub!**
