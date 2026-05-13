# 🤝 Contributing to Control Smart Devices

Thank you for your interest in contributing to the Enterprise Smart Home Automation Platform.

We welcome contributions from developers, IoT engineers, designers, testers, and open-source contributors.

---

# 🚀 Ways to Contribute

You can contribute by:

- Fixing bugs
- Improving UI/UX
- Adding new smart device integrations
- Improving automation features
- Writing documentation
- Adding tests
- Optimizing performance
- Enhancing security
- Improving Docker deployment
- Adding AI/ML smart automation

---

# 📂 Project Structure

```text
control-smart-devices/

├── mobile_app/
├── backend/
├── iot/
├── docker-compose.yml
└── README.md
```

---

# 🛠 Development Setup

## 1️⃣ Fork Repository

Fork the repository to your GitHub account.

---

## 2️⃣ Clone Repository

```bash
git clone https://github.com/bundlab/control-smart-devices.git
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## 4️⃣ Install Dependencies

### Backend

```bash
cd backend
pip install -r requirements.txt
```

### Mobile App

```bash
cd ../mobile_app
pip install -r requirements.txt
```

---

# 🚀 Running the Project

## Start Backend

```bash
cd backend
uvicorn app.main:app --reload
```

---

## Start Mobile App

```bash
cd mobile_app/app
python main.py
```

---

## Docker Deployment

```bash
docker compose up --build
```

---

# 🌿 Git Workflow

Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

Example:

```bash
git checkout -b feature/add-motion-sensor
```

---

# ✅ Commit Guidelines

Use clear commit messages.

Examples:

```bash
git commit -m "Add MQTT motion sensor integration"
```

```bash
git commit -m "Improve KivyMD dashboard UI"
```

```bash
git commit -m "Fix PostgreSQL device query bug"
```

---

# 🔥 Pull Request Process

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# 🧪 Testing

Run tests before submitting PRs.

```bash
pytest
```

---

# 📏 Code Style

## Python

- Follow PEP 8
- Use descriptive variable names
- Add docstrings where necessary

---

## KivyMD UI

- Keep UI responsive
- Maintain Material Design consistency

---

## FastAPI

- Use routers properly
- Keep endpoints modular
- Validate request schemas

---

# 🔐 Security Guidelines

Please avoid committing:

- `.env` files
- API keys
- MQTT passwords
- Database credentials
- Secret tokens

---

# 📡 Supported Technologies

- Python
- KivyMD
- FastAPI
- PostgreSQL
- MQTT
- Docker
- ESP32
- Raspberry Pi

---

# 💡 Contribution Ideas

You can help add:

- Voice assistant support
- Smart camera integration
- Energy analytics
- AI automation
- Firebase notifications
- Face recognition
- Cloud sync
- Home Assistant integration

---

# 🐛 Reporting Bugs

When reporting issues include:

- Operating system
- Python version
- Error logs
- Steps to reproduce
- Screenshots if applicable

---

# ⭐ Feature Requests

Feature suggestions are welcome.

Open an issue with:

- Feature description
- Use case
- Expected behavior

---

# 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

# ❤️ Thank You

Thank you for contributing to the Enterprise Smart Home Automation Platform.
Your support helps improve the future of smart IoT systems.