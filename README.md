# 🛍️ Django Barter Platform

This is a web application built with Django that allows users to post advertisements and propose item exchanges (barter system). Authenticated users can create ads, send barter proposals to other users, and manage proposal statuses.

---

## 📌 Features

- User registration & login (with Django's authentication)
- Post, edit, and delete ads
- Propose exchanges between ads
- Prevent users from proposing on their own ads
- Accept or reject proposals (only by the receiver)
- Admin interface for managing ads and proposals

---

## 🧱 Tech Stack

- **Backend:** Django 5.2
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default)
- **Deployment Ready:** Yes (via Gunicorn, etc.)

---

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/barter-platform.git
cd barter-platform
```

2. **Create Virtual Environment**

```bash
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply Migrations**

```bash
python manage.py migrate
```

5. **Create Superuser (Admin)**

```bash
python manage.py createsuperuser
```

6. **Run Development Server**

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠️ Project Structure

```
barter-platform/
│
├── ads_app/                 # Main Django app
│   ├── models.py            # Ad and ExchangeProposal models
│   ├── views.py             # Views (create ad, proposals, etc.)
│   ├── forms.py             # Model forms
│   ├── templates/           # HTML templates
│   └── admin.py             # Admin customization
│
├── barter_platform/         # Project config
│   ├── urls.py              # URL routes
│   └── settings.py          # Django settings
│
├── db.sqlite3               # SQLite database
├── manage.py
└── requirements.txt         # Python dependencies
```

---

## 📸 Screenshots

> You can add screenshots of:
> - Ad listing page
> - Proposal form
> - Admin dashboard

---

## ✅ TODO / Improvements

- Add messaging/notification system
- Implement image uploads
- Add pagination and search to ads
- REST API (with Django REST Framework)
- Unit & integration tests

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Tillo Khan – [Telegram](https://t.me/your_username)