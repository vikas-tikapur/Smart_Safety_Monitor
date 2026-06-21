# 🛡️ Smart Safety Monitor

A real-time **AI-powered Workplace Safety Monitoring System** built using **Python**, **OpenCV**, and **YOLOv8**.

The application monitors live webcam footage and detects workplace safety violations such as **persons**, **mobile phones**, and (upcoming) **helmets**, **safety vests**, and **weapons**. It also captures evidence, logs events, and provides a professional monitoring interface.

---

# Features

## Implemented

* Real-Time Webcam Monitoring
* YOLOv8 Object Detection
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
* Modular Project Architecture
* Well-Documented Source Code

---

## Upcoming Features

* Helmet Detection
* Safety Vest Detection
* Weapon Detection
* Dashboard Analytics
* Event Statistics
* Safety Alerts
* Custom YOLOv8 PPE Model
* Performance Optimization

---

# Project Structure

```text
Smart_Safety_Monitor/
│
├── dashboard/
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

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/vikas-tikapur/Smart_Safety_Monitor.git

cd Smart_Safety_Monitor
```

---

## 2. Create a virtual environment

```bash
py -3.10 -m venv venv
```

---

## 3. Activate virtual environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the application

```bash
python main.py
```

---

# AI Models

| Model        | Purpose                        | Status |
| ------------ | ------------------------------ | :----: |
| YOLOv8 COCO  | Person & Mobile Detection      |    ✅   |
| PPE Model    | Helmet & Safety Vest Detection |   🚧   |
| Weapon Model | Gun & Knife Detection          |   🚧   |

---

# Current Progress

| Feature                   | Status |
| ------------------------- | :----: |
| Project Setup             |    ✅   |
| Modular Project Structure |    ✅   |
| Camera Module             |    ✅   |
| YOLOv8 Model Loader       |    ✅   |
| Person Detection          |    ✅   |
| Person Counter            |    ✅   |
| Mobile Phone Detection    |    ✅   |
| Mobile Phone Counter      |    ✅   |
| Smart Screenshot Capture  |    ✅   |
| CSV Event Logging         |    ✅   |
| Live FPS Counter          |    ✅   |
| Professional Status Panel |    ✅   |
| Live Date & Time          |    ✅   |
| Helmet Detection          |   🚧   |
| Safety Vest Detection     |   🚧   |
| Weapon Detection          |   🚧   |
| Dashboard Analytics       |   🚧   |

---

# Project Goals

* Improve workplace safety using AI.
* Detect safety violations in real time.
* Capture screenshots as evidence.
* Generate CSV event logs.
* Build a modular and maintainable computer vision application.
* Train and integrate custom YOLOv8 models.
* Develop a professional AI monitoring dashboard.

---

# Current Version

## **v0.4.0 — Professional Monitoring UI**

### Completed

* Person Detection
* Mobile Phone Detection
* Smart Screenshot Capture
* CSV Event Logging
* Professional Monitoring Panel
* Live FPS Counter
* Live Date & Time

### In Progress

* Helmet Detection
* Safety Vest Detection
* Weapon Detection
* Dashboard Analytics

---

# Author

**Vikas Mishra**

GitHub:

https://github.com/vikas-tikapur
