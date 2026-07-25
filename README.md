# 🚀 ShopSphere - Dockerized Flask API with MySQL & Redis

![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Python](https://img.shields.io/badge/Python-3.12-yellow)
![Flask](https://img.shields.io/badge/Flask-REST_API-black)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![Docker Compose](https://img.shields.io/badge/Docker--Compose-Multi--Container-green)

---

# 📌 Project Overview

ShopSphere is a production-style Dockerized Flask REST API developed as a DevOps learning project.

The application demonstrates how multiple containers communicate together using Docker Compose.

The backend fetches product information from MySQL and improves response time using Redis caching.

This project simulates a real production microservice architecture.

---

# 🎯 Project Objectives

- Learn Docker
- Learn Docker Compose
- Learn Multi-container Architecture
- Learn Flask API
- Learn MySQL Integration
- Learn Redis Caching
- Learn Docker Networking
- Learn Docker Volumes
- Learn Production Debugging

---

# 🏗 Architecture

```
                    Client

                       │

                       ▼

              Flask REST API

                 (Container)

               /             \

              ▼               ▼

     MySQL Container     Redis Container

              │

        Docker Volume

              │

     Persistent Database
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Backend |
| Flask | REST API |
| Docker | Containerization |
| Docker Compose | Multi-container |
| MySQL 8 | Database |
| Redis | Cache |
| Docker Network | Container Communication |
| Docker Volume | Persistent Storage |

---

# 📂 Project Structure

```
shopsphere-docker-project/

│

├── backend/

│   ├── app.py

│   ├── db.py

│   ├── cache.py

│   ├── Dockerfile

│   ├── docker-compose.yml

│   ├── requirements.txt

│

├── screenshots/

│

├── README.md

├── architecture.md

├── api-documentation.md

├── docker-commands.md

├── troubleshooting.md

├── interview-questions.md

├── best-practices.md

├── learning-outcomes.md

└── project-flow.md
```

---

# ⚙ Features

✅ REST API

✅ Dockerized Application

✅ MySQL Database

✅ Redis Cache

✅ Docker Compose

✅ Persistent Storage

✅ Docker Networking

✅ Health Check API

✅ Product API

---

# 📡 API Endpoints

## Home API

```
GET /
```

Response

```json
{
    "application":"ShopSphere API",
    "version":"3.0",
    "message":"MySQL + Redis"
}
```

---

## Health API

```
GET /health
```

Response

```json
{
    "status":"Healthy"
}
```

---

## Products API

```
GET /products
```

Response

```json
[
    {
        "id":1,
        "name":"Laptop",
        "price":65000
    },
    {
        "id":2,
        "name":"Mechanical Keyboard",
        "price":4500
    }
]
```

---

# 🐳 Docker Containers

The project contains three containers.

```
shopsphere-backend

shopsphere-mysql

shopsphere-redis
```

---

# 🌐 Docker Network

```
shopsphere-network
```

All containers communicate using Docker DNS.

Example

```
backend

↓

mysql

↓

redis
```

---

# 💾 Docker Volume

```
mysql-data
```

Used for persistent MySQL storage.

Even if the container is deleted, database data remains safe.

---

# 🚀 How to Run

Clone repository

```
git clone https://github.com/yourusername/shopsphere-docker-project.git
```

Go inside project

```
cd shopsphere-docker-project/backend
```

Build containers

```
docker compose build
```

Run containers

```
docker compose up -d
```

Verify

```
docker compose ps
```

Open browser

```
http://localhost:5000
```

---

# 🔍 Verify Running Containers

```
docker ps
```

Expected

```
shopsphere-backend

shopsphere-mysql

shopsphere-redis
```

---

# 📷 Screenshots

Include screenshots for

- Docker Containers
- Docker Compose
- Browser Output
- Products API
- Redis Logs
- MySQL Logs

Store them inside

```
screenshots/
```

---

# 📚 What I Learned

✔ Docker Images

✔ Docker Containers

✔ Docker Compose

✔ Docker Network

✔ Docker Volumes

✔ Flask REST API

✔ MySQL Integration

✔ Redis Cache

✔ Docker Debugging

✔ Production Troubleshooting

---

# 🧪 Commands Used

```
docker build

docker run

docker images

docker ps

docker logs

docker exec

docker network ls

docker volume ls

docker compose up

docker compose down

docker compose ps

docker compose logs
```

---

# 🚨 Problems Solved

During this project I solved

- MySQL Authentication Error

- Docker Network Issues

- Decimal JSON Serialization Error

- Table Doesn't Exist Error

- Redis Cache Errors

- Internal Server Errors

- Docker Compose Troubleshooting

---

# 💼 Real Industry Concepts

This project demonstrates

- Multi-container Deployment

- Database Connectivity

- Docker Networking

- Service Discovery

- Caching Strategy

- Persistent Storage

- Container Debugging

- REST API Development

---

# 🔮 Future Improvements

- JWT Authentication

- User Login

- Product CRUD

- Shopping Cart

- Orders API

- Kubernetes Deployment

- Jenkins CI/CD

- GitHub Actions

- Nginx Reverse Proxy

- Prometheus Monitoring

- Grafana Dashboard

---

# 👨‍💻 Author

Monis

AWS DevOps Engineer (Learning)

Building production-ready DevOps projects using Docker, Kubernetes, Jenkins, Terraform, AWS and Python.

---

# ⭐ If you like this repository

Please give it a ⭐ on GitHub.

It motivates me to build more production-ready DevOps projects.
