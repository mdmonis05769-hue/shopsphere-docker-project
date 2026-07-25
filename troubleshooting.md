# 🛠 ShopSphere Troubleshooting Guide

## Overview

During the development of ShopSphere, multiple real-world Docker and application issues were encountered and resolved.

This document records the problems, root causes, debugging process, and solutions.

It demonstrates practical troubleshooting skills used by DevOps Engineers.

---

# DevOps Troubleshooting Workflow

Whenever an application fails, always follow this order.

```
Application Error

↓

docker ps

↓

docker ps -a

↓

docker logs

↓

docker compose logs

↓

docker inspect

↓

Application Code

↓

Database

↓

Network

↓

Volume

↓

Fix
```

Never start debugging from the browser.

Always start with Docker.

---

# Issue 1

## Flask Module Not Found

### Error

```
ModuleNotFoundError:
No module named 'flask'
```

### Root Cause

The Docker image was built with an empty `requirements.txt`, so Flask was never installed inside the container.

### Debugging

```
docker logs shopsphere-backend
```

### Fix

```
pip freeze > requirements.txt

docker build --no-cache -t shopsphere-backend:v1 .
```

---

# Issue 2

## Container Exited Immediately

### Symptoms

```
docker ps
```

Backend container missing.

```
docker ps -a
```

Container status:

```
Exited (1)
```

### Debugging

```
docker logs shopsphere-backend
```

### Root Cause

Application crashed during startup.

### Resolution

Read logs.

Fix Python code.

Rebuild Docker image.

---

# Issue 3

## MySQL Authentication Failed

### Error

```
Access denied for user
```

### Root Cause

Incorrect database credentials.

### Debugging

```
docker logs shopsphere-backend
```

Check

```
db.py
```

Verify MySQL user.

```
SHOW GRANTS;
```

### Resolution

Create user.

Grant privileges.

Reconnect backend.

---

# Issue 4

## Backend Could Not Connect to MySQL

### Error

```
Can't connect to MySQL
```

### Root Cause

Backend and MySQL were not on the same Docker network.

### Debugging

```
docker network ls

docker inspect shopsphere-network
```

### Resolution

Run backend using

```
--network shopsphere-network
```

or use Docker Compose.

---

# Issue 5

## Products Table Missing

### Error

```
Table 'shopsphere.products'
doesn't exist
```

### Root Cause

Database existed but table had not been created.

### Debugging

```
SHOW TABLES;
```

### Resolution

```
CREATE TABLE products(...);

INSERT INTO products(...);
```

---

# Issue 6

## Decimal JSON Serialization

### Error

```
Object of type Decimal
is not JSON serializable
```

### Root Cause

MySQL returned Decimal objects.

Python JSON cannot serialize Decimal directly.

### Resolution

Convert Decimal into float before calling

```
json.dumps()
```

---

# Issue 7

## Internal Server Error (500)

### Symptoms

Browser displayed

```
500 Internal Server Error
```

### Debugging

```
docker compose logs backend
```

Never debug from browser.

Always read backend logs.

### Resolution

Identify stack trace.

Fix application.

Rebuild image.

---

# Issue 8

## Docker Compose Backend Not Running

### Symptoms

```
docker compose ps
```

Backend service missing.

### Root Cause

Build failed or backend exited.

### Debugging

```
docker compose logs backend
```

### Resolution

```
docker compose up -d --build
```

---

# Issue 9

## Browser Connection Refused

### Error

```
ERR_CONNECTION_REFUSED
```

### Root Cause

Backend container not running.

### Debugging

```
docker ps
```

### Resolution

Restart container.

```
docker compose up -d
```

---

# Issue 10

## Redis Cache Not Working

### Symptoms

Every request queried MySQL.

### Debugging

```
docker logs backend
```

Expected

```
Cache MISS

Cache HIT
```

### Resolution

Correct Redis connection.

Verify cache key.

---

# Common Docker Commands

View running containers

```bash
docker ps
```

---

View stopped containers

```bash
docker ps -a
```

---

Container logs

```bash
docker logs shopsphere-backend
```

---

Compose logs

```bash
docker compose logs backend
```

---

Inspect

```bash
docker inspect shopsphere-backend
```

---

Networks

```bash
docker network ls
```

---

Volumes

```bash
docker volume ls
```

---

# Production Debugging Checklist

Before saying "Application is broken", verify:

- Docker Engine running
- Container running
- Image exists
- Correct Docker Network
- Correct Volume
- Database running
- Redis running
- Environment variables
- Port mapping
- Container logs
- Application logs

---

# Lessons Learned

During this project I learned how to troubleshoot:

- Docker Images
- Containers
- Docker Compose
- MySQL Authentication
- Docker Networks
- Redis Cache
- Flask Runtime Errors
- JSON Serialization
- Missing Database Tables
- Internal Server Errors

---

# Real DevOps Workflow

```
Developer reports issue

↓

DevOps Engineer

↓

Check Docker

↓

Read Logs

↓

Identify Root Cause

↓

Apply Fix

↓

Rebuild

↓

Restart

↓

Verify

↓

Close Incident
```

---

# Interview Tip

When explaining this project in an interview, don't only say:

> "I built a Docker project."

Instead explain:

> "While building the project I diagnosed multiple production-style issues including Docker image build failures, MySQL authentication errors, Docker networking problems, missing database tables, JSON serialization issues, and Redis cache integration. I used Docker logs, Docker Compose logs, Docker inspect, Docker networks, and MySQL debugging commands to identify and resolve each issue."

This demonstrates real troubleshooting ability, which is a core DevOps skill.
