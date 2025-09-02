# 🏨 Airbnb Clone

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/) 
[![SQLite](https://img.shields.io/badge/SQLite-3.43-lightgrey?logo=sqlite&logoColor=white)](https://www.sqlite.org/) 

A **web application for hotel booking and blogging**, built with **Python & Django**.  
Users can **sign up, confirm email, manage profile, search hotels, book rooms, and explore blogs**. Admins can manage all content via the **Django dashboard**.

---

## 📋 Table of Contents

- [✨ Features](#-features)  
- [🛠️ Technologies](#️-technologies)  
- [⚙️ Installation](#️-installation)  
- [🚀 Usage Flow](#-usage-flow)  
- [🖼️ Screenshots](#️-screenshots)  
- [🔮 Future Plans](#-future-plans)  
- [👤 Author](#-author)  

---

## ✨ Features

- **🔐 User Authentication:** Signup with email confirmation, user profiles with picture and info.  
- **🔎 Hotel Search:** Search by name, location, or category.  
- **🏨 Hotel Listings:** Users can add hotels; each hotel has details, photos, and availability.  
- **📅 Booking System:** Select date & number of guests to book rooms.  
- **📝 Blog Section:** Add, search, view posts by tags/categories/keywords, and comment with Discuss.  
- **🛠️ Admin Dashboard:** Manage hotels, blog posts, FAQs, contacts, and site content.  
- **📞 Contact & About Pages:** View FAQs, contact the site, and learn about the platform.

---

## 🛠️ Technologies

- **Backend:** Python, Django  
- **Database:** SQLite  
- **Authentication:** Django Allauth  
- **API:** Django REST Framework  
- **Editor:** Summernote  
- **Discussion System:** Discuss  
- **Others:** Pillow, Whitenoise, Virtualenv, Gunicorn  

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/mos8afa/airbnb.git
cd airbnb

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations & create superuser
python manage.py migrate
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver

# 6. Open browser at http://127.0.0.1:8000/
```

## 🚀 Usage Flow

1- Signup → Email Confirmation → Profile

2- Search Hotels → View Details → Book Room

3- Blog Section → Read/Add Posts → Comment

4- Admin Dashboard → Manage Content


## 🔮 Future Plans

💳 Add a payment system for bookings
🏨 Implement hotel room management (add rooms & availability)
⭐ Add room and hotel rating system

👤 Author

Mostafa Rashwan
GitHub: https://github.com/mos8afa