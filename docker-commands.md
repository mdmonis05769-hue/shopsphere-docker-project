# 🐳 Docker Commands Reference

## Overview

This document contains the Docker and Docker Compose commands used during the ShopSphere project.

It serves as a quick reference for development, troubleshooting, and interviews.

---

# Check Docker Version

```bash
docker --version
```

Example

```
Docker version 28.x.x
```

---

# Check Docker Information

```bash
docker info
```

Shows:

- Docker Engine
- Storage Driver
- Networks
- Volumes
- Containers
- Images

---

# Docker Images

## List Images

```bash
docker images
```

---

## Build Image

```bash
docker build -t shopsphere-backend:v1 .
```

Explanation

- `-t` → Tag image
- `shopsphere-backend` → Image name
- `v1` → Version
- `.` → Current directory

---

## Remove Image

```bash
docker rmi shopsphere-backend:v1
```

---

# Docker Containers

## Run Container

```bash
docker run -d \
--name shopsphere-backend \
-p 5000:5000 \
shopsphere-backend:v1
```

---

## List Running Containers

```bash
docker ps
```

---

## List All Containers

```bash
docker ps -a
```

---

## Stop Container

```bash
docker stop shopsphere-backend
```

---

## Start Container

```bash
docker start shopsphere-backend
```

---

## Restart Container

```bash
docker restart shopsphere-backend
```

---

## Remove Container

```bash
docker rm shopsphere-backend
```

---

## Force Remove

```bash
docker rm -f shopsphere-backend
```

---

# Docker Logs

View logs

```bash
docker logs shopsphere-backend
```

---

Follow logs

```bash
docker logs -f shopsphere-backend
```

---

Last 50 lines

```bash
docker logs --tail=50 shopsphere-backend
```

---

# Execute Commands Inside Container

Open shell

```bash
docker exec -it shopsphere-backend bash
```

For MySQL

```bash
docker exec -it shopsphere-mysql mysql -u root -p
```

---

# Docker Networks

List

```bash
docker network ls
```

---

Inspect

```bash
docker network inspect shopsphere-network
```

---

Create

```bash
docker network create shopsphere-network
```

---

Delete

```bash
docker network rm shopsphere-network
```

---

# Docker Volumes

List

```bash
docker volume ls
```

---

Create

```bash
docker volume create mysql-data
```

---

Inspect

```bash
docker volume inspect mysql-data
```

---

Delete

```bash
docker volume rm mysql-data
```

---

# Docker Compose

Start

```bash
docker compose up -d
```

---

Build Again

```bash
docker compose up -d --build
```

---

Stop

```bash
docker compose stop
```

---

Start Existing Containers

```bash
docker compose start
```

---

Restart

```bash
docker compose restart
```

---

Shutdown

```bash
docker compose down
```

---

Shutdown and Remove Volumes

```bash
docker compose down -v
```

---

List Services

```bash
docker compose ps
```

---

Compose Logs

```bash
docker compose logs
```

Backend Logs

```bash
docker compose logs backend
```

Live Logs

```bash
docker compose logs -f backend
```

---

# Docker Inspect

Inspect Container

```bash
docker inspect shopsphere-backend
```

Inspect Image

```bash
docker image inspect shopsphere-backend:v1
```

---

# Docker History

```bash
docker history shopsphere-backend:v1
```

Shows all image layers.

---

# Docker Statistics

```bash
docker stats
```

Shows

- CPU
- Memory
- Network
- Block I/O

---

# Docker Cleanup

Remove stopped containers

```bash
docker container prune
```

---

Remove unused images

```bash
docker image prune
```

---

Remove unused volumes

```bash
docker volume prune
```

---

Remove unused networks

```bash
docker network prune
```

---

Complete cleanup

```bash
docker system prune
```

Remove everything

```bash
docker system prune -a
```

---

# MySQL Commands

Login

```bash
docker exec -it shopsphere-mysql mysql -u root -p
```

Show databases

```sql
SHOW DATABASES;
```

Select database

```sql
USE shopsphere;
```

Show tables

```sql
SHOW TABLES;
```

View products

```sql
SELECT * FROM products;
```

Exit

```sql
exit;
```

---

# Redis Commands

Open Redis CLI

```bash
docker exec -it shopsphere-redis redis-cli
```

Set value

```bash
SET name ShopSphere
```

Read value

```bash
GET name
```

List keys

```bash
KEYS *
```

Exit

```bash
exit
```

---

# Troubleshooting Commands

Container not running

```bash
docker ps -a
```

---

Application logs

```bash
docker logs shopsphere-backend
```

---

Compose logs

```bash
docker compose logs backend
```

---

Check network

```bash
docker network inspect shopsphere-network
```

---

Check volume

```bash
docker volume inspect mysql-data
```

---

Check
