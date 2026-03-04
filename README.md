# HRMS Lite – Employee & Attendance Management System

HRMS Lite is a simple **Employee and Attendance Management System** built using **React (TypeScript)** for the frontend and **Django REST Framework** for the backend.  
It allows managing employees and marking daily attendance through a clean dashboard interface.

---

# Tech Stack

### Frontend

- React
- TypeScript
- Axios
- React Router
- React Toastify
- CSS

### Backend

- Django
- Django REST Framework
- PostgreSQL

### Tools

- Git
- GitHub
- Render (PostgreSQL hosting)

---

# Features

## Employee Management

- Add new employee
- Edit employee details
- Delete employee
- View employee list
- Form validation
- Toast notifications for success/errors

## Attendance Management

- Mark daily attendance
- Employee dropdown selection
- Prevent duplicate attendance
- Delete attendance records
- Display employee name instead of ID

## Dashboard

- Navigation sidebar
- Overview page

---

# Project Architecture

# HRMS Lite – Employee & Attendance Management System

HRMS Lite is a simple **Employee and Attendance Management System** built using **React (TypeScript)** for the frontend and **Django REST Framework** for the backend.  
It allows managing employees and marking daily attendance through a clean dashboard interface.

---

# Tech Stack

### Frontend

- React
- TypeScript
- Axios
- React Router
- React Toastify
- CSS

### Backend

- Django
- Django REST Framework
- PostgreSQL

### Tools

- Git
- GitHub
- Render (PostgreSQL hosting)

---

# Features

## Employee Management

- Add new employee
- Edit employee details
- Delete employee
- View employee list
- Form validation
- Toast notifications for success/errors

## Attendance Management

- Mark daily attendance
- Employee dropdown selection
- Prevent duplicate attendance
- Delete attendance records
- Display employee name instead of ID

## Dashboard

- Navigation sidebar
- Overview page

---

# Project Architecture

React Frontend
↓
Axios API Calls
↓
Django REST APIs
↓
Serializers (Validation Layer)
↓
Models (Database Interaction)
↓
PostgreSQL Database

---

# Backend Folder Structure

│ ├── views.py
│ └── urls.py
│
├── employees
│ ├── migrations
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── config
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .env

---

# Frontend Folder Structure

hrms-frontend
│
├── src
│ ├── api
│ │ └── axiosConfig.ts
│ │
│ ├── components
│ │
│ ├── layouts
│ │ └── MainLayout.tsx
│ │
│ ├── pages
│ │ ├── Dashboard.tsx
│ │ ├── Employees.tsx
│ │ └── Attendance.tsx
│ │
│ ├── routes
│ │ └── AppRoutes.tsx
│ │
│ ├── types
│ │ ├── employee.ts
│ │ └── attendance.ts
│ │
│ ├── App.tsx
│ └── index.tsx
│
└── package.json

---

# Database Schema

## Employee Table

| Field       | Type        |
| ----------- | ----------- |
| id          | Primary Key |
| employee_id | String      |
| full_name   | String      |
| email       | String      |
| department  | String      |
| created_at  | DateTime    |

---

## Attendance Table

| Field      | Type                 |
| ---------- | -------------------- |
| id         | Primary Key          |
| employee   | ForeignKey(Employee) |
| date       | Date                 |
| status     | Present / Absent     |
| created_at | DateTime             |

---

# API Endpoints

## Employee APIs

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| GET    | `/api/employees/`      | Get employee list |
| POST   | `/api/employees/`      | Create employee   |
| PUT    | `/api/employees/{id}/` | Update employee   |
| DELETE | `/api/employees/{id}/` | Delete employee   |

---

## Attendance APIs

| Method | Endpoint                | Description            |
| ------ | ----------------------- | ---------------------- |
| GET    | `/api/attendance/`      | Get attendance records |
| POST   | `/api/attendance/`      | Mark attendance        |
| DELETE | `/api/attendance/{id}/` | Delete attendance      |

---

# Backend Setup

Clone repository

git clone <repository-url>
cd hrms-backend

Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Start server

python manage.py runserver

Backend runs on

http://127.0.0.1:8000

---

# Frontend Setup

Navigate to frontend folder

cd hrms-frontend

Install dependencies

npm install

Start application

npm start

Frontend runs on

http://localhost:3001

---

# Environment Variables

Create `.env` file inside backend project:

DATABASE_URL=postgresql://user:password@host:port/database

---

# Application Flow

## Add Employee

User fills employee form
↓
React sends POST request
↓
Django API validates data
↓
Data stored in PostgreSQL
↓
Frontend fetches updated list
↓
Employee table updates

---

## Mark Attendance

User selects employee from dropdown
↓
Select date and status
↓
POST request to /attendance/
↓
Backend saves record
↓
Frontend reloads attendance list

---

Project URL Link

Frontend Repo:
https://github.com/akshay2123/hrms-frontend

Backend Repo:
https://github.com/akshay2123/hrms-backend

---

# Error Handling

- Backend returns validation errors
- Frontend displays errors using **React Toastify**
- Duplicate employee email or ID validation supported

---

# Future Improvements

- Authentication system
- Role-based access control
- Attendance analytics dashboard
- Employee search and filtering
- Export attendance reports

---

# Author

Akshay Kale  
Full Stack Developer  
React | Django | PostgreSQL

---

# License

This project is created for learning and demonstration purposes.
