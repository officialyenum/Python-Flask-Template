# Python Flask Starter Template

![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Realtime-Socket.IO-ffca28?logo=socketdotio&logoColor=black)

A minimal yet scalable **Flask** template to help developers kickstart new projects **without the hassle of repetitive setup**.  
Designed for clean organization, modularity, and quick extension.

## 🚀 Features

- Clear separation of concerns (controllers, routes, models, templates, configs)
- Easy-to-extend base structures
- Pre-built login page and base HTML templates
- Centralized app, database, and event configuration

## 🛠 Project Structure

```
src/
├── app.py            # Entry point
├── config/           # Configuration classes
│   ├── app.py        # App setup
│   ├── config.py     # Environment configs
│   ├── database.py   # Database setup
│   └── events.py     # Event listeners / hooks
│
├── controller/       # Base controllers
│   └── base_controller.py
│
├── routes/           # Routes definitions
│   └── users.py      # Example user routes
│
├── models/           # Database models
│   └── user.py
│
└── templates/        # Jinja2 templates
    ├── base.html     # Base structure
    └── login.html    # Login page
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
  Create route files inside `src/routes/` and register your endpoints.

- **Create Controllers:**  
  Extend the base controller from `src/controller/` for common functionalities.

- **Define Models:**  
  Add your database models in `src/models/`.

- **Templates:**  
  Customize `base.html` and add new Jinja2 templates inside `src/templates/`.

- **Configuration:**  
  Update or add new configs in `src/config/` to suit your environment needs.

---

## 📄 Example

Example: a simple user route.

```python
# src/routes/users.py

from flask import Blueprint
user_bp = Blueprint('users', __name__)

@user_bp.route('/users')
def list_users():
    return {"users": ["user1", "user2"]}
```

Register the blueprint in `src/app.py`:

```python
from routes.users import user_bp

app.register_blueprint(user_bp)
```

---

## 🔥 Planned Improvements
- CLI generator for new modules (routes, models, etc.)
- Authentication system built-in
- Docker support
- Testing suite with Pytest

---

## 📜 License

This project is licensed under the MIT License.
