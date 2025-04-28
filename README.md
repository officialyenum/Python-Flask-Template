# Python Micro Flask Starter Template

A minimal yet scalable **Flask** template to help developers kickstart new projects **without the hassle of repetitive setup**.  
Designed for clean organization, modularity, and quick extension.

![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Realtime-Socket.IO-ffca28?logo=socketdotio&logoColor=black)


![Flask](https://img.shields.io/badge/Flask-Framework-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![SocketIO](https://img.shields.io/badge/RealTime-Socket.IO-ff69b4)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

## 🚀 Features

- Clear separation of concerns (controllers, routes, models, templates, configs)
- Easy-to-extend base structures
- Pre-built login page and base HTML templates
- Centralized app, database, and event configuration

## 🚀 Introduction

This is a minimal, ready-to-use **Flask microservice template** designed to help developers **start building quickly** without worrying about setup.  
It supports both **basic Flask apps** and **real-time applications with Socket.IO**.  
Auto-detects **MongoDB** and **SQL (PostgreSQL, SQLite)** based on your configuration.

Perfect for:
- APIs
- Real-time apps (chat, live updates)
- Scalable microservices

---

## 🏗️ Project Structure

```
src/
├── app.py                # Main entry point
├── config/
│   ├── app.py             # App class (core setup)
│   └── config.py          # Environment configs
├── event/                 # Events if using socket io
├── controller/            # Base controllers (extendable)
├── service/               # Base services (extendable)
├── routes/                # All route modules (auto-registered)
│   ├── __init__.py
│   ├── api.py
│   └── web.py
├── models/                # Database models
├── templates/             # Login & base HTML templates
└── static/                # Static assets (CSS, JS, images)
```

---

## ⚡ Features

- 🔥 Auto-detect MongoDB (PyMongo) or SQL (SQLAlchemy) from config
- 🔥 Auto-discover and register all route blueprints
- 🔥 Flask-SocketIO integration (for real-time WebSocket support)
- 🔥 Clean MVC structure (Controller / Model / View)
- 🔥 Support for CORS and multiple environments (dev, prod)
- 🔥 Minimal, fast, ready to deploy

---

## 📦 Requirements

- Python 3.10+
- Flask
- Flask-SocketIO
- Flask-PyMongo
- Flask-SQLAlchemy
- Eventlet or Gevent (for Socket.IO production use)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/officialyenum/Python-Flask-Template.git
cd Python-Flask-Template
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
python src/app.py
```

---

## 🧩 How To Use

- **Add Routes:**  
  Modify api and web route files inside `src/routes/` and register your endpoints.

- **Create Controllers:**  
  Extend the base controller from `src/controller/` for common functionalities.

- **Define Models:**  
  Add your database models in `src/models/`.

- **Templates:**  
  Customize `base.html` and add new Jinja2 templates inside `src/templates/`.

- **Configuration:**  
  Update or add new configs in `src/config/` to suit your environment needs.

---

---

## ⚙️ Configuration

Create your environment config inside `src/config/config.py`.  
Example:

```python
class DevelopmentConfig:
    DEBUG = True
    
    # MongoDB example
    MONGO_URI = "mongodb://localhost:27017/yourdb"

    # OR SQL database example
    # SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/yourdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

You can modify multiple environments config class like `ProductionConfig`, `TestingConfig`, etc.

---

## 🚀 Running the App

### 1. Run with Flask (basic HTTP):

```python
# src/app.py
from config.app import App

if __name__ == "__main__":
    app = App.get_app('development')
    app.run_app()
```

---

### 2. Run with Socket.IO (WebSocket support):

```python
# src/app.py
from config.app import App

if __name__ == "__main__":
    app = App.get_app('development')
    app.run_with_socketio()
```

---

## 🛠 Adding New Routes

Simply write api and web routes in `src/routes/`, for example: `routes/api.py` or `routes/web.py`

```python
from flask import Blueprint

bp = Blueprint('blog', __name__)

@bp.route('/blog')
def blog_home():
    return "Welcome to the Blog!"
```

✅ Done! No need to manually register — the template auto-discovers your blueprint.

---

## 🔥 Build on Top of It

You can easily add:
- Controllers in `/controller/`
- Models in `/models/`
- Views (HTML templates) in `/templates/`
- Static assets (CSS/JS) in `/static/`

Ready to scale as your app grows.

---

## 🧠 Credits

Created with ❤️ to make Flask development **faster**, **cleaner**, and **more scalable**.

---

## 🔥 Planned Improvements
- CLI generator for new modules (routes, models, etc.)
- Authentication system built-in
- Docker support
- Testing suite with Pytest

---

## 📣 Feedback & Collaboration
This is a solo development project, but I’m always open to feedback, ideas, or potential collaboration. If you're into python fullstack web development, feel free to open an issue or fork the project!

## 📜 License

This project is licensed under the MIT License.
# 🚀 Happy Building!




