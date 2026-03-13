# Cafe Inventory Management API (ENG-6)

## Overview

This project implements a **Cafe Inventory Management** using **Django** and **Django REST Framework**.
It allows users to manage cafe inventory by performing standard CRUD operations such as adding, retrieving, updating, and deleting products.

Additionally, the system includes an **automated low-stock alert mechanism** that logs a warning whenever a product’s quantity falls below its defined threshold.


---

# Features

* Add new products to the inventory
* Retrieve all products or a specific product
* Update product details and stock levels
* Delete products from the inventory
* Automatic **low-stock alert logging**
* Data validation using serializers
* RESTful API endpoints

---

# Technology Stack

* Python
* Django
* Django REST Framework
* SQLite (development database)
* Python Logging

---

# Project Structure

```
cafe_inventory/
│
├── cafe_inventory/          # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── inventory/               # Inventory application
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

---

# Product Model

The system manages products with the following attributes:

| Field     | Description                        |
| --------- | ---------------------------------- |
| name      | Product name                       |
| category  | Product category                   |
| quantity  | Current stock level                |
| price     | Product price                      |
| threshold | Minimum stock level before warning |

---

# Low Stock Alert Mechanism

Whenever a product is created or updated through the API, the system checks whether:

```
quantity < threshold
```

If the condition is true, a **warning message is logged** in the server terminal.

Example:

```
WARNING: Low Stock Alert: Milk only has 4 left!
```

This logic is implemented inside:

```
inventory/services.py
```

---

# API Endpoints

| Method      | Endpoint            | Description              |
| ----------- | ------------------- | ------------------------ |
| POST        | /api/products/      | Create a new product     |
| GET         | /api/products/      | Retrieve all products    |
| GET         | /api/products/{id}/ | Retrieve product details |
| PATCH / PUT | /api/products/{id}/ | Update product           |
| DELETE      | /api/products/{id}/ | Delete product           |

---

# Installation & Setup

## 1. Clone Repository

```
git clone <repository-url>
cd cafe_inventory
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Apply Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Run Development Server

```
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

# Example Request

Create product

POST `/api/products/`

```
{
"name": "Coffee Beans",
"category": "Ingredients",
"quantity": 10,
"price": 30,
"threshold": 5
}
```

---

# Development Notes

* The project follows a **layered architecture** separating API logic, business logic, and database models.
* `services.py` contains business logic such as stock alerts.
* Serializers are used for **data validation and JSON conversion**.
* Logging is used to track low-stock warnings.

---
