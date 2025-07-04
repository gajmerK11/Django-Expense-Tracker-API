# 💸 Django Expense Tracker API

A secure, token-authenticated REST API for tracking personal income and expenses, built using Django and Django REST Framework.

---

## 📌 Project Features

- ✅ JWT-based user authentication (login, registration, token refresh)
- ✅ Automatic tax calculation (flat or percentage)
- ✅ Full CRUD support for expense/income records
- ✅ Paginated API responses
- ✅ Personal expense/income tracking

---

## 🛠️ Technologies Used

- Python 3.8+
- Django 3+
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (for development)

---

## 📁 Project Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/expense-tracker-api.git
   cd expense-tracker-api
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication (JWT)

### Register

```http
POST /api/auth/register/
```

**Request Body**

```json
{
  "username": "john",
  "password": "securepassword"
}
```

### Login

```http
POST /api/auth/login/
```

**Request Body**

```json
{
  "username": "john",
  "password": "securepassword"
}
```

**Response**

```json
{
  "refresh": "token_here",
  "access": "token_here"
}
```

### Refresh Token

```http
POST /api/auth/refresh/
```

**Request Body**

```json
{
  "refresh": "your_refresh_token"
}
```

---

## 💸 Expense/Income API Endpoints

All endpoints below require a JWT access token in the `Authorization` header:

```
Authorization: Bearer your_access_token
```

### Create a Record

```http
POST /api/expenses/
```

**Body**

```json
{
  "title": "Grocery",
  "description": "Weekly shopping",
  "amount": 100.0,
  "transaction_type": "debit",
  "tax": 10.0,
  "tax_type": "flat"
}
```

---

### List User's Records (Paginated)

```http
GET /api/expenses/
```

**Sample Response**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Grocery",
      "amount": 100.0,
      "tax": 10.0,
      "tax_type": "flat",
      "total": 110.0,
      "transaction_type": "debit",
      "created_at": "2025-01-01T10:00:00Z"
    }
  ]
}
```

---

### Retrieve a Record

```http
GET /api/expenses/{id}/
```

### Update a Record

```http
PUT /api/expenses/{id}/
```

### Delete a Record

```http
DELETE /api/expenses/{id}/
```

---

## 🧠 Business Logic

- **Flat tax**: `total = amount + tax`
- **Percentage tax**: `total = amount + (amount × tax ÷ 100)`

---

## 🛡️ Permissions

| Role            | Access Control              |
| --------------- | --------------------------- |
| Regular User    | Only their own records      |
| Superuser       | All records                 |
| Unauthenticated | Cannot access any endpoints |

---

## 🔎 Testing Checklist

- ✅ Register/login/refresh tokens
- ✅ Create & retrieve user-specific records
- ✅ Superuser sees all data
- ✅ 403/404 for unauthorized access
- ✅ Tax calculation logic validated
- ✅ Paginated response structure works

---

## 🧪 Example Test (Superuser Access)

```http
GET /api/expenses/
Authorization: Bearer <admin_token>
```

✅ Should return all records across users.

---

## ✅ Postman Test Cases (with Screenshots)

All test cases mentioned in the checklist have been manually tested using **Postman**. A complete visual report is provided in the [`test_case.pdf`](./test_case.pdf) file located in the root of this repository.

📄 **Contents of `test_case.pdf` include:**

- 🔐 User registration & login (valid/invalid)
- 🔄 Token refresh
- ✅ Authenticated and unauthenticated API access
- ✏️ CRUD operations (Create, Read, Update, Delete)
- 🔍 Permission tests (user vs superuser)
- 💰 Business logic validation (flat & percentage tax)

> 👉 **To view the test results**, open `test_case.pdf` from the GitHub repo or download it directly.

---

## 📬 Contact

> Internship Project by Kumar Gajmer  
> For queries, contact: gajmerk9@gmail.com
