# 🏠 Control Smart Devices

![Python](https://img.shields.io/badge/Python-3.12-blue)
![KivyMD](https://img.shields.io/badge/KivyMD-MobileApp-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![MQTT](https://img.shields.io/badge/MQTT-IoT-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Enterprise Smart Home Automation Platform

A professional smart home control system built with:

- 📱 KivyMD Mobile App
- ⚡ FastAPI Backend
- 🗄 PostgreSQL Database
- 📡 MQTT Communication
- 🐳 Docker Deployment
- 🤖 Automation Engine
- 📊 Real-Time Monitoring

---

# ✨ Features

## 🏠 Smart Home Control

- Light control
- Fan control
- Smart switches
- Device grouping
- Room management

---

## 📡 Sensor Monitoring

- Temperature monitoring
- Humidity monitoring
- Smoke detection
- Motion sensors
- Real-time updates

---

## ⚡ Automation Engine

- IF/THEN automation
- Smart schedules
- Sensor-triggered actions
- Auto device control

Example:

```python
IF temperature > 30:
    turn_on_fan()
```

---

# 📱 Mobile App Screens

- Splash Screen
- Login Screen
- Dashboard
- Devices
- Rooms
- Automation
- Analytics
- Profile

---

# 🧱 Technology Stack

| Layer | Technology |
|------|-------------|
| Mobile App | KivyMD |
| Backend API | FastAPI |
| Database | PostgreSQL |
| Communication | MQTT |
| Authentication | JWT |
| Containerization | Docker |
| IoT Devices | ESP32 / Raspberry Pi |

---

# 📂 Project Structure

```text
control-smart-devices/

├── mobile_app/
├── backend/
├── iot/
├── docker-compose.yml
├── CONTRIBUTING.md
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

# 1️⃣ Clone Repository

```bash
git clone https://github.com/bundlab/control-smart-devices.git
```

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

## Linux/macOS

```bash
source venv/bin/activate
```

## Windows

```bash
venv\\Scripts\\activate
```

---

# 3️⃣ Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

# 4️⃣ Install Mobile App Dependencies

```bash
cd ../mobile_app
pip install -r requirements.txt
```

---

# 🗄 PostgreSQL Setup

Create database:

```sql
CREATE DATABASE smart_home;
```

Update:

```python
DATABASE_URL = "postgresql://admin:password@localhost/smart_home"
```

---

# 🚀 Run Backend API

```bash
cd backend
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

# 📱 Run Mobile App

```bash
cd mobile_app/app
python main.py
```

---

# 🐳 Docker Deployment

## Start All Services

```bash
docker compose up --build
```

---

# 📡 MQTT Topics

| Topic | Description |
|------|-------------|
| home/light | Smart light control |
| home/fan | Fan control |
| home/temperature | Temperature sensor |
| home/motion | Motion detection |

---

# 🔐 Authentication

This system supports:

- JWT Authentication
- Role-Based Access
- Secure API Tokens
- Protected Routes

---

# 📈 Analytics Dashboard

Track:

- Power consumption
- Device activity
- Sensor history
- Energy usage
- Smart automation events

---

# 🤖 IoT Hardware Support

Supported devices:

- ESP32
- ESP8266
- Raspberry Pi
- Arduino
- MQTT Sensors

---

# 📱 Build Android APK

## Install Buildozer

```bash
pip install buildozer cython
```

---

## Build APK

```bash
buildozer android debug
```

APK output:

```text
bin/
```

---

# 🐳 Docker Services

Included containers:

- FastAPI Backend
- PostgreSQL Database
- MQTT Broker
- NGINX Reverse Proxy

---

# 🔥 Future Upgrades

Planned features:

- Voice assistant
- Face recognition
- Push notifications
- AI automation
- Google Home integration
- Alexa integration
- Cloud synchronization

---

# 🌍 Enterprise Use Cases

This platform can power:

1. Smart Homes
2. Smart Offices
3. Smart Hospitals
4. Smart Hotels
5. Smart Factories
6. Smart Farms
7. Smart Warehouses
8. Smart Schools
9. Energy Systems
10. Industrial IoT

---

# 🧪 Testing

Run backend tests:

```bash
pytest
```

---

# 📜 License

MIT License

---

# 👨‍💻 Author
Abdullahi Bundi

Built with ❤️ using Python, KivyMD, FastAPI, MQTT, and PostgreSQL.
