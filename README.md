# Blog API Project

This is a simple blog API built using Django and Django REST Framework, based on the **Django for APIs** tutorial by [William S. Vincent](https://wsvincent.com).

## 📌 Features

* Token-based authentication
* CRUD operations for blog posts
* Clean project structure following best practices
* Powered by Django REST Framework (DRF)

## 📁 Project Structure

```
blogapi/
├── blog_project/     # Django project settings
├── posts/            # Blog app with API logic
├── db.sqlite3        # SQLite database
├── manage.py         # Django management script
├── Pipfile           # Project dependencies
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Mechantchulo/blogapi.git
cd blogapi
```

### 2. Install Dependencies

Using pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create a Superuser (optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) to view the API.

## 🛠️ Technologies Used

* Django
* Django REST Framework
* SQLite
* Pipenv

## 📚 Reference

This project is based on the [Django for APIs](https://wsvincent.com/books/) book by **William S. Vincent**.

---

## ✨ Author

**Erick Mutua**

Feel free to fork, star, and contribute!
