# سیستم مدیریت امور دانشگاه (College Management System)

این پروژه با هدف طراحی و پیاده‌سازی یک سیستم ساده برای مدیریت امور دانشگاهی با استفاده از زبان Python و فریم‌ورک Flask توسعه داده شده است.

## امکانات پروژه

- ثبت‌نام دانشجویان
- انتخاب واحد درسی
- گزارش نمرات
- ارائه API برای مدیریت کاربران و وظایف

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

## اجرای پروژه بدون Docker

ابتدا Python 3.12 را نصب کنید.

سپس وابستگی‌های پروژه را نصب کنید:

```bash
pip install -r requirements.txt
```

برای اجرای برنامه از دستور زیر استفاده کنید:

```bash
python app.py
```

پس از اجرا، آدرس زیر را در مرورگر باز کنید:

```text
http://localhost:5000/
```

## اجرای پروژه با Docker

برای ساخت Docker Image از دستور زیر استفاده کنید:

```bash
docker build -t college-api .
```

برای اجرای Container:

```bash
docker run -d -p 5000:5000 --name college-container college-api
```

برای مشاهده Containerهای در حال اجرا:

```bash
docker ps
```

برای متوقف کردن Container:

```bash
docker stop college-container
```

برای حذف Container:

```bash
docker rm college-container
```

## مستندات API

اطلاعات مربوط به Endpointها، متدهای HTTP، کدهای وضعیت و دیاگرام معماری در فایل `API_CONTRACT.md` قرار داده شده است.

## وضعیت پروژه

بخش Back-End با استفاده از Flask پیاده‌سازی شده و فایل‌های پیکربندی Docker نیز آماده شده‌اند. ساخت Image و اجرای Container هنوز به‌صورت عملی آزمایش نشده است.

---

# College Management System

A simple College Management System project developed using Python and Flask.

## Project Features

- Student Registration
- Course Selection
- Grade Reporting
- REST API for Users and Tasks

## Technologies Used

- Python 3.12
- Flask 3.1.2
- Docker

## Project Structure

```text
College/
│
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

## Running the Application Without Docker

1. Install Python 3.12.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open the following address in your browser:

```text
http://localhost:5000/
```

## Docker Instructions

Build the Docker image:

```bash
docker build -t college-api .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name college-container college-api
```

Check running containers:

```bash
docker ps
```

Test the API:

```text
http://localhost:5000/
http://localhost:5000/api/users
http://localhost:5000/api/tasks
```

Stop the container:

```bash
docker stop college-container
```

Remove the container:

```bash
docker rm college-container
```

## API Documentation

The API endpoints, HTTP methods, status codes, and architecture diagram are documented in `API_CONTRACT.md`.

## Project Status

The Flask backend and Docker configuration files have been prepared. Docker image building and container execution have not yet been tested.
