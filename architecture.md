# 🏗 ShopSphere Architecture

## Overview

ShopSphere is a production-style multi-container application built using Docker Compose.

Instead of installing everything on one machine, every component runs inside its own container.

This architecture is similar to how modern applications are deployed in production.

---

# High Level Architecture

```
                +----------------------+
                |      Web Browser     |
                +----------+-----------+
                           |
                           |
                      HTTP Request
                           |
                           ▼
              +-------------------------+
              | Flask Backend Container |
              |    Port : 5000          |
              +-----------+-------------+
                          |
          +---------------+---------------+
          |                               |
          |                               |
          ▼                               ▼
+----------------------+        +----------------------+
|   MySQL Container    |        |   Redis Container    |
|     Port : 3306      |        |     Port : 6379      |
+----------+-----------+        +----------+-----------+
           |
           |
           ▼
+----------------------+
| Docker Volume        |
| mysql-data           |
+----------------------+
```

---

# Components

## 1. Flask Backend

Responsibilities

- Accept HTTP Requests
- Validate Request
- Read Cache
- Read Database
- Return JSON Response

Technology

```
Python
Flask
```

Container

```
shopsphere-backend
```

---

## 2. MySQL

Responsibilities

- Store Products
- Persistent Storage
- Execute SQL Queries

Technology

```
MySQL 8
```

Container

```
shopsphere-mysql
```

---

## 3. Redis

Responsibilities

- Cache Frequently Requested Data
- Improve Performance
- Reduce Database Load

Technology

```
Redis
```

Container

```
shopsphere-redis
```

---

## 4. Docker Network

Network Name

```
shopsphere-network
```

Purpose

Allows every container to communicate using service names.

Example

Instead of

```
172.20.0.3
```

we use

```
mysql
```

or

```
redis
```

Docker automatically resolves the hostname.

---

# Docker Compose Architecture

```
docker-compose.yml

        │

        ▼

Creates Network

        │

        ▼

Starts MySQL

        │

        ▼

Starts Redis

        │

        ▼

Builds Flask Image

        │

        ▼

Starts Backend Container
```

---

# Request Flow

When a client opens

```
GET /products
```

the following process happens.

```
Browser

↓

Flask

↓

Check Redis Cache

↓

Cache Hit ?

↓

YES ----------------→ Return Response

↓

NO

↓

Read MySQL

↓

Return Data

↓

Store Data in Redis

↓

Next Request becomes Cache Hit
```

---

# Redis Cache Flow

## First Request

```
Browser

↓

Flask

↓

Redis

↓

Not Found

↓

MySQL

↓

Products

↓

Redis Cache

↓

Browser
```

---

## Second Request

```
Browser

↓

Flask

↓

Redis

↓

Products Found

↓

Browser
```

No database query is executed.

---

# Database Flow

```
Flask

↓

MySQL Connection

↓

Execute SQL

↓

Receive Rows

↓

Convert JSON

↓

Return Client
```

---

# Docker Networking

Every container receives an internal IP address.

Example

```
Backend

↓

mysql:3306

↓

Redis:6379
```

The backend never needs to know the IP address.

Docker DNS handles communication automatically.

---

# Persistent Storage

Without Volume

```
Delete Container

↓

Database Deleted
```

With Volume

```
Delete Container

↓

Create New Container

↓

Database Still Exists
```

Volume Used

```
mysql-data
```

---

# Project Directory Architecture

```
shopsphere-docker-project

│

├── backend

│   ├── app.py

│   ├── db.py

│   ├── cache.py

│   ├── Dockerfile

│   ├── docker-compose.yml

│

├── screenshots

│

├── README.md

├── architecture.md

├── api-documentation.md

├── troubleshooting.md

├── docker-commands.md

├── interview-questions.md

├── best-practices.md

└── learning-outcomes.md
```

---

# Production Deployment Flow

```
Developer

↓

GitHub

↓

Jenkins

↓

Docker Build

↓

Docker Image

↓

Docker Compose

↓

Backend

↓

MySQL

↓

Redis

↓

Users
```

---

# Advantages of This Architecture

- Isolated services
- Easy deployment
- Faster development
- Reproducible environment
- Easy scaling
- Easy debugging
- Supports CI/CD integration
- Production ready foundation

---

# Real Company Use Case

Most e-commerce applications use the same architecture.

Example

```
Frontend

↓

Backend API

↓

Redis Cache

↓

MySQL Database

↓

Persistent Storage
```

Additional services are commonly added in production:

- Nginx
- Jenkins
- Kubernetes
- Prometheus
- Grafana
- ELK Stack
- AWS Load Balancer

---

# Key Learning Outcomes

After completing this project you understand:

- Multi-container applications
- Docker Compose architecture
- Container networking
- Docker DNS
- Redis caching
- MySQL integration
- Persistent storage
- REST API flow
- Request lifecycle
- Production deployment concepts
