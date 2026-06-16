<div align="center">

<img src="images/amboLogo.PNG" alt="Ambo University Logo" width="120"/>

# 🎓 Smart University System

### AI-Powered Campus Intelligence & Security Platform

*Ambo University — Computer Science Department*

---

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PySide](https://img.shields.io/badge/PySide2%2F6-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![License](https://img.shields.io/badge/License-Academic-orange?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)]()

---

> **A comprehensive, vision-powered campus management platform** combining face recognition, vehicle monitoring, PC asset tracking, and real-time security surveillance — all in a single unified desktop application.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Module Breakdown](#-module-breakdown)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [Known Issues & Limitations](#-known-issues--limitations)
- [Roadmap](#-roadmap)
- [Ethical Considerations](#-ethical-considerations)
- [Author](#-author)

---

## 🌟 Overview

The **Smart University System** is a desktop application developed for **Ambo University** that automates and secures campus operations through artificial intelligence. Built with Python and a Qt-based GUI, it provides administrators with real-time monitoring of people, vehicles, and assets across campus.

The system integrates **live camera feeds**, **face recognition**, **PC asset verification**, and **access control** into a single, role-protected interface — reducing manual overhead while enhancing institutional security.

---

## ✨ Key Features

### 🔐 Secure Authentication
- Frameless, modern login window with drag-to-move support
- Credential validation against a MySQL `superadminlogin` table
- Animated splash screen with progressive loading feedback

### 👤 Student Registration & Face Enrollment
- Full personal profile capture: name, age, DOB, department, gender, nationality, phone, address
- **Live face capture** using OpenCV + Haar Cascade — images saved as `data/student/<username>.<id>.jpg`
- Registered records displayed in a live-updating `QTableWidget`

### 🖥️ PC Asset Management
- Assign laptops/computers to registered students via **face recognition at the time of registration**
- Stores PC name, serial number, and links back to the student record
- Updates the `register` table with a `pc` ownership flag upon successful asset binding

### 🚗 Vehicle Registration
- Dedicated `CarRegister` module with a custom `.ui` layout
- Placeholder architecture ready for license plate recognition integration

### 📷 Outdoor Surveillance Dashboard
- Four-camera live feed panel supporting simultaneous streams
- Toggle panels for: **All Cameras**, **Weapon Detection**, **PC Recognition**, **Vehicle Recognition**, **Face Recognition**
- `SimpleFacerec` engine runs at **25% frame resolution** for real-time performance

### 🧠 Face Recognition Engine (`SimpleFacerec`)
- Bulk-loads all student face encodings from disk on startup
- Per-frame: resize → BGR→RGB → locate faces → encode → compare → identify
- Returns `(face_locations, face_names)` with graceful `"unknown"` fallback
- Uses **smallest face distance** (not first match) for highest accuracy

### 🏛️ Super Admin Dashboard
- Animated sidebar with slide-in/out navigation (250ms easing curve)
- Card-based home screen with drop-shadow buttons for: Student Register, PC Register, Admin, Vehicle, Cafeteria, Servant
- Stacked-widget pages for Home, Register, and Face Recognition views

---

## 🏗️ System Architecture

```
smart-university-system/
│
├── Splash.py                        # Entry point — animated loading screen
├── Login.py                         # Authentication window
├── SuperAdmin.py                    # Main dashboard & navigation hub
│
├── Register.py                      # Student registration + face photo capture
├── PcRegister.py                    # PC asset assignment via face scan
├── CarRegister.py                   # Vehicle registration (scaffold)
│
├── Outdoor_Face_recognition.py      # Multi-camera surveillance dashboard
├── simple_facerec.py                # Core face recognition engine
├── button_control.py                # UI toggle helpers
│
├── haarcascade_frontalface_default.xml   # Face detection model (OpenCV)
│
├── *_ui.py                          # Auto-generated Qt UI Python bindings
├── *.ui                             # Qt Designer layout files
│
└── images/                          # Application assets & icons
    ├── amboLogo.PNG
    ├── carIcon.png
    ├── computerIcon (1).png
    └── ...
```

### Application Flow

```
[Splash.py]  →  Progress bar animation (0–100%)
     ↓
[Login.py]   →  MySQL credential check
     ↓
[SuperAdmin.py]  →  Animated sidebar dashboard
     ├── [Register.py]              Student enrollment + face capture
     ├── [PcRegister.py]            PC asset binding via face scan
     ├── [CarRegister.py]           Vehicle registration
     └── [Outdoor_Face_recognition.py]  Live surveillance panels
                    └── [simple_facerec.py]   Recognition engine
```

---

## 📦 Module Breakdown

| File | Class | Responsibility |
|------|-------|----------------|
| `Splash.py` | `splash` | Animated startup screen with QTimer progress loop |
| `Login.py` | `Login` | Frameless auth window; MySQL login validation |
| `SuperAdmin.py` | `SuperAdmin` | Main hub; animated sidebar, card navigation |
| `Register.py` | `Register` | Student form + Haar Cascade face capture to disk |
| `PcRegister.py` | `PcRegister` | Face scan → auto-fill form → link PC to student |
| `CarRegister.py` | `carRegister` | Vehicle registration UI scaffold |
| `Outdoor_Face_recognition.py` | `Outdoor_Face_recognition` | 4-panel live camera dashboard + panel toggles |
| `simple_facerec.py` | `SimpleFacerec` | Bulk-encode, detect, identify faces in video frames |
| `button_control.py` | *(functions)* | Reusable widget show/hide toggle helpers |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **GUI Framework** | PySide2 / PySide6 (Qt) | All windows, layouts, animations |
| **Computer Vision** | OpenCV (`cv2`) | Camera capture, frame processing, Haar Cascade detection |
| **Face Recognition** | `face_recognition` (dlib) | Encoding, matching, identification |
| **Database** | MySQL + `mysql-connector-python` | User, asset, and attendance records |
| **Data** | NumPy | Face location array math and distance calculations |
| **UI Design** | Qt Designer (`.ui` files) | Drag-and-drop layout authoring |
| **Asset Detection** | Haar Cascade XML | Fast frontal face detection for enrollment |

---

## 🗄️ Database Schema

**Database name:** `ambo_university`

```sql
-- Admin authentication
CREATE TABLE superadminlogin (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    username  VARCHAR(100) NOT NULL,
    password  VARCHAR(255) NOT NULL
);

-- Student registry
CREATE TABLE register (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    first_name      VARCHAR(100),
    father_name     VARCHAR(100),
    grandfather_name VARCHAR(100),
    username        VARCHAR(100) UNIQUE,
    age             VARCHAR(10),
    DOB             VARCHAR(20),
    department      VARCHAR(100),
    gender          VARCHAR(20),
    photo           VARCHAR(255),     -- path: data/student/<username>.<id>.jpg
    phone_number    VARCHAR(20),
    nationality     VARCHAR(50),
    address         VARCHAR(255),
    pc              VARCHAR(50)       -- 'havepc' / NULL
);

-- PC asset registry
CREATE TABLE pcregister (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    first_name      VARCHAR(100),
    father_name     VARCHAR(100),
    grandfather_name VARCHAR(100),
    pc_name         VARCHAR(100),
    serial_number   VARCHAR(100),
    username        VARCHAR(100),
    age             VARCHAR(10),
    DOB             VARCHAR(20),
    department      VARCHAR(100),
    gender          VARCHAR(20),
    phone_number    VARCHAR(20),
    address         VARCHAR(255)
);
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server 8.x
- Webcam / USB camera
- Git

### Step 1 — Clone the repository

```bash
git clone https://github.com/<your-username>/smart-university-system.git
cd smart-university-system
```

### Step 2 — Create a virtual environment

```bash
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install PySide2 PySide6 opencv-python face_recognition mysql-connector-python numpy
```

> **Note on `face_recognition`:** This library requires `cmake` and `dlib`. On Windows, install [CMake](https://cmake.org) and [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) first. On Linux: `sudo apt install cmake build-essential libboost-all-dev`.

### Step 4 — Set up the database

```bash
# Log into MySQL and run:
mysql -u root -p
```

```sql
CREATE DATABASE ambo_university;
USE ambo_university;

-- Paste the schema from the section above, then:

INSERT INTO superadminlogin (username, password) VALUES ('admin', 'your_secure_password');
```

### Step 5 — Create face data directories

```bash
mkdir -p data/student
```

### Step 6 — Run the application

```bash
python Splash.py
```

---

## ⚙️ Configuration

### Database credentials

Credentials are currently hardcoded across modules. Before deploying, replace them with environment variables:

```python
# Current (insecure — for development only)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jhon1995",        # ⚠️ Change this
    database="ambo_university"
)
```

**Recommended:** Create a `.env` file and use `python-dotenv`:

```env
# .env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password_here
DB_NAME=ambo_university
```

```python
# In code
import os
from dotenv import load_dotenv
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
```

Add `.env` to `.gitignore` immediately.

### Face data path

```python
# In Register.py — face images are saved here:
file_name_path = "data/student/" + f"{Username}.{img_id}" + ".jpg"

# In PcRegister.py — face encodings are loaded from:
sfr.load_encoding_images("data/")
```

---

## 📖 Usage Guide

### Launching the system

1. Start MySQL service
2. Run `python Splash.py`
3. The splash screen animates to 100%, then opens the Login window

### Registering a student

1. From the Super Admin dashboard, click **Student Register**
2. Fill in all personal details
3. Click **Add Photo** — your webcam opens and captures the student's face
4. Click **Save** to store the record in the database

### Assigning a PC to a student

1. From the Super Admin dashboard, click **PC Register**
2. Click **Scan Face** — the system identifies the student via webcam
3. Personal details auto-fill from the database
4. Enter PC name and serial number, then click **Save**

### Monitoring with cameras

1. From the Super Admin dashboard, click **Face Recognition**
2. The 4-panel camera view opens
3. Use the top buttons to toggle individual feeds: All / Face / PC / Vehicle / Weapon

---

## ⚠️ Known Issues & Limitations

| Issue | Description | Severity |
|-------|-------------|----------|
| **Hardcoded DB credentials** | `password="jhon1995"` appears in 5+ files | 🔴 Critical |
| **SQL injection risk** | `PcRegister.py` uses f-string queries directly | 🔴 Critical |
| **Import inconsistency** | `Login.py` uses PySide6; other modules use PySide2 | 🟡 Medium |
| **Missing `mysql` import** in `Login.py` | `mysql.connector` is used but not imported | 🟡 Medium |
| **Global `file_name_path`** | Used across `Register.py` methods without initialization guard | 🟡 Medium |
| **Blocking camera loop** | `face_recog()` in surveillance module blocks the main Qt thread | 🟡 Medium |
| **`close()` method override** | `PcRegister.close()` overrides `QMainWindow.close()`, breaking window closure | 🟡 Medium |
| **`CarRegister.py` incomplete** | No logic implemented beyond displaying the window | 🟢 Low |
| **Single camera used for 4 feeds** | All four panels read from `cap1` on VideoCapture(0) | 🟢 Low |

---

## 🗺️ Roadmap

- [ ] Replace hardcoded credentials with `.env` / config file
- [ ] Parameterize all SQL queries to prevent injection
- [ ] Unify PySide2 → PySide6 across all modules
- [ ] Move camera loops to `QThread` workers to prevent UI freezing
- [ ] Integrate YOLOv8 for weapon and vehicle detection
- [ ] Add license plate OCR to `CarRegister` module
- [ ] Implement attendance log export (CSV / PDF)
- [ ] Add role-based access: Super Admin vs. regular Admin
- [ ] Add unit tests for `SimpleFacerec` and DB operations
- [ ] Package as a standalone `.exe` with PyInstaller

---

## 🔒 Ethical Considerations

This project was developed for **academic and research purposes** under the supervision of Ambo University's Computer Science Department.

- All face data is stored locally and is never transmitted externally
- The system is designed for **institutional use only** — not public deployment
- No real student data has been included in this repository
- The weapon detection module is intended as a safety alert tool, not a surveillance instrument
- Users and administrators should comply with applicable privacy laws before deploying any biometric system

---

## 👨‍💻 Author

<div align="center">

**Jhonson Ayalew**
Computer Science Graduate — Ambo University
*Specialization: Data, Automation & Computer Vision*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github)](https://github.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com)

</div>

---

<div align="center">

*Built with ❤️ at Ambo University, Ethiopia*

**© 2024 Jhonson Ayalew — All Rights Reserved**

</div>
