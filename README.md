# LogRock-Challenge- # Insurance Policy API

This is a REST API for managing insurance policies using Django and Django REST Framework (DRF).

## Features

- Create a new policy
- Retrieve a list of all policies
- Retrieve details of a specific policy
- Update an existing policy
- Delete a policy

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository_url>
cd LogRock-Challenge-
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python insurance_company/manage.py migrate
```

### 5. Run the Server
```bash
python insurance_company/manage.py runserver
```

The API will be available at:  
`http://127.0.0.1:8000/`

---

## **Project Structure**

```plaintext
insurance_company/      # Main Django project directory
│── api/                # API application directory
│   │── migrations/     # Database migration files
│   │── __init__.py     # Indicates that this directory is a Python module
│   │── admin.py        # Django admin configuration
│   │── apps.py         # App configuration
│   │── models.py       # Database models definition
│   │── serializer.py   # Serializers for data conversion
│   │── tests.py        # Automated tests
│   │── urls.py         # API endpoint routes
│   │── views.py        # API logic and views
│
│── insurance_company/  # Django project settings
│   │── __init__.py     
│   │── asgi.py         # ASGI configuration
│   │── settings.py     # Project settings (Database, Apps, Middleware, etc.)
│   │── urls.py         # Global project URLs
│   │── wsgi.py         # WSGI configuration
│
│── manage.py           # Django management script
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
```


## **API Endpoints**

### 1. Get All Policies
**Endpoint:** `GET /api/policies/`  
**Response:**
```json
[
  {
    "policy_id": 1,
    "customer_name": "Jose Mendes",
    "policy_type": "auto",
    "expiry_date": "2026-05-15"
  }
]
```

### 2. Create a New Policy
**Endpoint:** `POST /api/policies/`  
**Request Body:**
```json
{
  "customer_name": "Mariana Souza",
  "policy_type": "home",
  "expiry_date": "2025-11-30"
}
```
**Response:**
```json
{
  "policy_id": 2,
  "customer_name": "Mariana Souza",
  "policy_type": "home",
  "expiry_date": "2025-11-30"
}
```

### 3. Retrieve a Specific Policy
**Endpoint:** `GET /api/policies/{id}/`  
**Response:**
```json
{
  "policy_id": 2,
  "customer_name": "Mariana Souza",
  "policy_type": "home",
  "expiry_date": "2025-11-30"
}
```

### 4. Update a Policy
**Endpoint:** `PUT /api/policies/{id}/`  
**Request Body:**
```json
{
  "customer_name": "Mariana Souza",
  "policy_type": "auto",
  "expiry_date": "2026-02-20"
}
```
**Response:**
```json
{
  "policy_id": 2,
  "customer_name": "Mariana Souza",
  "policy_type": "auto",
  "expiry_date": "2026-02-20"
}
```

### 5. Delete a Policy
**Endpoint:** `DELETE /api/policies/{id}/`  
**Response:**
```json
{
  "message": "Policy deleted successfully"
}
```

