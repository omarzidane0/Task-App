# Task-AppA

simple task management app for demonstration purposes only.

# 📝 Task App

**A Flask-based task management web application**  
This project showcases how to create, edit, and track tasks using a Flask back end, SQLite database, JWT-based authentication, CSRF protection, and a Blueprint-structured MVC (Model-View-Controller) pattern.

---
![image](https://github.com/user-attachments/assets/48adf85b-7361-4cef-8697-ebeca26f7c42)
![image](https://github.com/user-attachments/assets/a2fe7d07-3269-4261-b53f-07dcf0ff3b13)
![image](https://github.com/user-attachments/assets/d82bf416-7adc-40d0-b8a0-0ee8938c755e)




---

## 💡 Features

- **User Registration & Login**  
  • Password hashing (e.g., Werkzeug)  
  • JWT-based authentication (access tokens)  
  • CSRF protection on forms (Flask-WTF)  

- **Task CRUD (Create, Read, Update, Delete)**  
  • Create new tasks with title, description, creation date, and deadline  
  • Edit existing tasks (Blueprint-based views)  
  • Mark tasks as completed  
  • Delete tasks  

- **Countdown & Time Tracking**  
  • Calculate remaining time until each task’s deadline (in hours, minutes, seconds)  
  • Show creation timestamp (date & time)  
  • Automatically highlight overdue tasks in red  

- **Blueprint-Based MVC Structure**  
  • **Models**: SQLAlchemy ORM models defining `User` and `Task` tables (SQLite)  
  • **Views (Controllers)**: Separate view-functions in Blueprints (`register_bp`, `login_bp`, `home_bp`)  
  • **Templates**: Jinja2 HTML templates

- **Email/Session Management (Optional)**  
  • Flask session for temporary data storage (e.g., flash messages)  
  • (You can later expand to email-based password resets, etc.)

- **Responsive Frontend**  
  • Bootstrap 5 (or Tailwind CSS) for styling and responsive layout  


---

## 🛠️ Technologies & Libraries Used

| Layer            | Description                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Language**     | Python 3.x                                                                                                                       |
| **Web Framework**| [Flask](https://flask.palletsprojects.com/) (microframework)                                                                    |
| **Database ORM** | [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) (with SQLite as the development database)                      |
| **Authentication**| [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/) for creating and decoding access tokens (JWT)                 |
| **Forms & CSRF** | [Flask-WTF](https://flask-wtf.readthedocs.io/) (WTForms integration) + **CSRFProtect** for form validation & CSRF protection     |
| **Templating**   | [Jinja2](https://jinja.palletsprojects.com/) with **ChoiceLoader & FileSystemLoader** to load templates from multiple folders |
| **Project Structure**| **Blueprints** for modular MVC-like organization (each blueprint handles a “domain”: registration, login, home/tasks)       |
| **Database Engine**| SQLite (via SQLAlchemy). Easy setup for development; switchable to PostgreSQL/MySQL in production via URI in `Config`.       |
| **Configuration**| Custom `Config` class (in `app/config.py`) to centralize settings (SECRET_KEY, JWT settings, SQLALCHEMY_DATABASE_URI, etc.)       |


---

## 📂 Project Structure

├── app
│   ├── config.py
│   ├── extension.py
│   ├── models
│   │   └── models.py
│   ├── routes
│   │   ├── home
│   │   │   ├── home.py
│   │   │   ├── static
│   │   │   │   ├── css
│   │   │   │   └── js
│   │   │   │       └── homescript.js
│   │   │   ├── templates
│   │   │   │   └── home.html
│   │   │
│   │   ├── login
│   │   │   ├── login.py
│   │   │   ├── static
│   │   │   │   ├── css
│   │   │   │   └── js
│   │   │   │       └── loginscript.js
│   │   │   ├── templates
│   │   │   │   └── login.html
│   │   │
│   │   ├── register
│   │   │   ├── register.py
│   │   │   ├── static
│   │   │   │   ├── css
│   │   │   │   └── js
│   │   │   │       └── register_script.js
│   │   │   ├── templates
│   │   │   │   └── register.html
│   │   │
│   │   └── templates
│   │       ├── 404.html
│   │       ├── base.html
│   │       ├── footer.html
│   │       ├── header.html
│   │       └── headers.css
│   ├── utils
│   │   ├── jwt_utils.py
│   │   ├── password_utils.py
│   ├── __init__.py
├── app.py
├── instance
│   └── test.db
├── README.txt
└── requierments.txt
