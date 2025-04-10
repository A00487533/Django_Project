# 🏨 Hotel Booking Backend - Django

This is the backend API for managing hotel listings in a hotel booking system, built using Django. It currently supports adding new hotels via a POST request.

## 📦 Features
- Create hotel entries with details such as:
  - Name
  - Price
  - Location
  - Availability
- JSON-based API for easy frontend integration

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/A00487533/Django_Project.git
cd Django_Project
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🧩 Models

### Hotel Model
Defined in `models.py`:
```python
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

## 🚀 API Endpoints

### ➕ Create a Hotel

**Endpoint:** `/api/create-hotel/`  
**Method:** `POST`  
**Content-Type:** `application/json`

#### 🔸 Sample Request
```json
{
  "name": "Skyline Inn",
  "price": "129.99",
  "location": "Halifax, Canada",
  "availability": true
}
```

#### 🔸 Sample Response (201 Created)
```json
{
  "message": "Hotel created successfully.",
  "hotel": {
    "id": 1,
    "name": "Skyline Inn",
    "price": "129.99",
    "location": "Halifax, Canada",
    "availability": true
  }
}
```

#### 🔸 Error Response Example
```json
{
  "error": "Missing required fields."
}
```

## 🧪 Test with `curl`
```bash
curl -X POST http://localhost:8000/api/create-hotel/ \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Skyline Inn",
           "price": "129.99",
           "location": "Halifax, Canada",
           "availability": true
         }'
```

## 🗂 URL Configuration

In `urls.py`:
```python
from django.urls import path
from .views import create_hotel

urlpatterns = [
    path('api/create-hotel/', create_hotel, name='create_hotel'),
]
```

## 📌 Notes
- CSRF protection is disabled for this endpoint (`@csrf_exempt`) for testing purposes. Add token handling in production.
- Currently only `POST` is supported. Additional CRUD features can be added later.


