# سیستم مدیریت امور دانشگاه (College Management System)

این پروژه یک سیستم ساده مدیریت امور دانشگاهی است که با استفاده از Python و فریم‌ورک Flask توسعه داده شده است. بخش Backend پروژه به‌صورت REST API طراحی شده و با استفاده از Docker قابل اجرا است.

## امکانات پروژه

- مدیریت کاربران (Users)
- مدیریت وظایف (Tasks)
- ثبت‌نام دانشجویان
- انتخاب واحد درسی
- گزارش نمرات
- ارائه REST API

## تکنولوژی‌های استفاده‌شده

- Python 3.12
- Flask 3.1.2
- Docker

## ساختار پروژه

```text
College/
├── app.py
├── course.py
├── registration.py
├── report.py
├── requirements.txt
├── API_CONTRACT.md
├── Dockerfile
├── .dockerignore
└── README.md
```

## اجرای پروژه با Docker

برای اجرای پروژه ابتدا باید Docker Desktop نصب و اجرا شده باشد.

### 1. دریافت پروژه

Repository را از GitHub دریافت کنید:

```bash
git clone https://github.com/INZIII86/College.git
```

وارد پوشه پروژه شوید:

```bash
cd College
```

### 2. ساخت Docker Image

با اجرای دستور زیر، Image پروژه ساخته می‌شود:

```bash
docker build -t college-api .
```

### 3. اجرای Docker Container

برای اجرای پروژه داخل یک Container از دستور زیر استفاده کنید:

```bash
docker run -d -p 5000:5000 --name college-container college-api
```

در این دستور، پورت 5000 کامپیوتر به پورت 5000 داخل Container متصل می‌شود.

### 4. بررسی وضعیت Container

برای مشاهده Containerهای در حال اجرا:

```bash
docker ps
```

### 5. تست API

پس از اجرای موفق Container، آدرس‌های زیر را در مرورگر باز کنید:

صفحه اصلی API:

```text
http://localhost:5000/
```

دریافت فهرست کاربران:

```text
http://localhost:5000/api/users
```

دریافت فهرست وظایف:

```text
http://localhost:5000/api/tasks
```

### 6. متوقف کردن و حذف Container

برای متوقف کردن Container:

```bash
docker stop college-container
```

برای حذف Container:

```bash
docker rm college-container
```

## مستندات API

اطلاعات مربوط به Resourceها، Endpointها، متدهای HTTP، کدهای وضعیت و دیاگرام معماری در فایل `API_CONTRACT.md` قرار دارد.

## نکته

اطلاعات کاربران و وظایف در نسخه فعلی به‌صورت موقت در حافظه برنامه ذخیره می‌شوند و با راه‌اندازی مجدد برنامه به حالت اولیه برمی‌گردند.

## وضعیت پروژه

Backend پروژه با Flask پیاده‌سازی شده و فایل‌های موردنیاز Docker شامل `Dockerfile` و `.dockerignore` آماده شده‌اند. دستورات ساخت Image و اجرای Container نیز در این مستندات ارائه شده‌اند.

---

# College Management System

A simple College Management System developed using Python and Flask. The backend is designed as a REST API and can be deployed using Docker.

## Project Features

- User Management
- Task Management
- Student Registration
- Course Selection
- Grade Reporting
- REST API

## Technologies Used

- Python 3.12
- Flask 3.1.2
- Docker

## Project Structure

```text
College/
├── app.py
├── course.py
├── registration.py
├── report.py
├── requirements.txt
├── API_CONTRACT.md
├── Dockerfile
├── .dockerignore
└── README.md
```

## Running the Project with Docker

Docker Desktop must be installed and running before starting the project.

### 1. Clone the Repository

```bash
git clone https://github.com/INZIII86/College.git
```

Navigate to the project directory:

```bash
cd College
```

### 2. Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t college-api .
```

### 3. Run the Docker Container

Start the application inside a Docker container:

```bash
docker run -d -p 5000:5000 --name college-container college-api
```

### 4. Check the Container Status

To check running containers:

```bash
docker ps
```

### 5. Test the API

After starting the container, open the following URLs in your browser:

Main API endpoint:

```text
http://localhost:5000/
```

Get all users:

```text
http://localhost:5000/api/users
```

Get all tasks:

```text
http://localhost:5000/api/tasks
```

### 6. Stop and Remove the Container

Stop the container:

```bash
docker stop college-container
```

Remove the container:

```bash
docker rm college-container
```

## API Documentation

API resources, endpoints, HTTP methods, status codes, and the architecture diagram are documented in `API_CONTRACT.md`.

## Note

User and task data are currently stored in memory and will reset when the application restarts.

## Project Status

The Flask backend has been implemented, and Docker configuration files (`Dockerfile` and `.dockerignore`) have been prepared. Docker build and run commands are documented above.
