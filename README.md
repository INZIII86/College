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
