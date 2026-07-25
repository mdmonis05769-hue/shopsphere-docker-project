# 💼 Docker & DevOps Interview Questions

## Overview

This document contains commonly asked Docker and DevOps interview questions based on the ShopSphere project.

The answers are written in a professional yet easy-to-understand manner.

---

# 1. What is Docker?

### Answer

Docker is an open-source containerization platform that packages an application along with its dependencies into a container. This ensures the application runs consistently across development, testing, and production environments.

---

# 2. Why did you use Docker in the ShopSphere project?

### Answer

Docker allowed me to package the Flask application, MySQL database, and Redis cache into separate containers. This created a consistent development environment and simplified deployment using Docker Compose.

---

# 3. What is the difference between a Virtual Machine and a Docker Container?

| Virtual Machine | Docker Container |
|-----------------|------------------|
| Includes full operating system | Shares host operating system kernel |
| Heavyweight | Lightweight |
| Slow startup | Fast startup |
| Uses more memory | Uses less memory |
| Hypervisor required | Docker Engine required |

---

# 4. What is a Docker Image?

### Answer

A Docker image is a read-only template containing the application code, runtime, libraries, dependencies, and configuration needed to create a Docker container.

---

# 5. What is a Docker Container?

### Answer

A Docker container is a running instance of a Docker image. It executes the application in an isolated environment.

---

# 6. What is a Dockerfile?

### Answer

A Dockerfile is a text file containing instructions used to build a Docker image.

Example instructions include:

- FROM
- WORKDIR
- COPY
- RUN
- EXPOSE
- CMD

---

# 7. What is Docker Compose?

### Answer

Docker Compose is a tool used to define and manage multi-container Docker applications using a single `docker-compose.yml` file.

In ShopSphere, Docker Compose starts:

- Flask Backend
- MySQL
- Redis

with one command.

```bash
docker compose up -d
```

---

# 8. Why did you use Redis?

### Answer

Redis was used as an in-memory cache to reduce database queries and improve response time for frequently requested product data.

---

# 9. What is Docker Networking?

### Answer

Docker networking allows containers to communicate with each other securely.

For example:

```
Backend
   │
   ├── mysql
   └── redis
```

The backend accesses services using container names instead of IP addresses.

---

# 10. What are Docker Volumes?

### Answer

Docker volumes provide persistent storage. Even if the MySQL container is removed, the database remains available because the data is stored in a named volume.

---

# 11. Why did you use Docker Compose instead of running containers manually?

### Answer

Docker Compose simplifies deployment by managing all services, networks, and volumes from one configuration file, making the environment reproducible.

---

# 12. What is the purpose of the EXPOSE instruction?

### Answer

`EXPOSE` documents the port the application listens on inside the container.

Example:

```dockerfile
EXPOSE 5000
```

---

# 13. What is the difference between COPY and ADD?

### Answer

`COPY` copies local files into the image.

`ADD` can also extract local archives and download remote URLs, but `COPY` is preferred for most use cases because it is more predictable.

---

# 14. What is the difference between CMD and ENTRYPOINT?

| CMD | ENTRYPOINT |
|------|------------|
| Provides default command | Defines the main executable |
| Can be overridden easily | Usually remains fixed |

---

# 15. How did the ShopSphere request flow work?

```
Browser
    │
    ▼
Flask API
    │
    ▼
Redis Cache
    │
Cache Hit?
 ├── Yes → Return Response
 └── No
      ▼
    MySQL
      ▼
 Store in Redis
      ▼
 Return Response
```

---

# 16. How did you debug container issues?

### Answer

I followed a structured process:

1. Check running containers.
2. Review container logs.
3. Inspect the container.
4. Verify Docker network.
5. Verify database connectivity.
6. Rebuild and restart if needed.

Useful commands:

```bash
docker ps
docker logs
docker compose logs
docker inspect
```

---

# 17. What problems did you solve during this project?

### Answer

I resolved:

- MySQL authentication errors
- Missing database tables
- Docker networking issues
- JSON serialization errors
- Backend startup failures
- Redis cache configuration issues
- Internal server errors

---

# 18. How does Docker improve CI/CD?

### Answer

Docker provides consistent build artifacts that can be tested and deployed in any environment, reducing "works on my machine" problems and enabling reliable CI/CD pipelines.

---

# 19. What is Docker Layer Caching?

### Answer

Each Dockerfile instruction creates a layer. Docker reuses unchanged layers during rebuilds, making builds much faster.

---

# 20. Why should secrets not be hardcoded?

### Answer

Hardcoding credentials is a security risk. Environment variables or dedicated secrets management tools should be used instead.

---

# Practical Commands Frequently Asked

```bash
docker images
docker ps
docker ps -a
docker logs
docker exec
docker inspect
docker network ls
docker volume ls
docker compose up -d
docker compose down
docker compose ps
docker stats
docker system prune
```

---

# Scenario-Based Questions

## A container keeps restarting. What would you do?

### Answer

- Check `docker ps -a`
- Read logs using `docker logs`
- Verify environment variables
- Check application startup errors
- Rebuild if necessary

---

## MySQL cannot be reached from the backend. How would you investigate?

### Answer

- Confirm MySQL container is running.
- Check Docker network.
- Verify service name.
- Test database credentials.
- Review backend logs.

---

## Why is Redis useful in an e-commerce application?

### Answer

Redis stores frequently requested data in memory, reducing database load and improving response times.

---

# Best Practices

- Use official base images.
- Keep images small.
- Pin dependency versions.
- Use Docker Compose for multi-container projects.
- Store secrets securely.
- Monitor logs regularly.
- Use named volumes for databases.
- Document every project.

---

# How to Explain This Project in an Interview

> "I developed a production-style Flask REST API and containerized it using Docker. The application uses Docker Compose to orchestrate three containers: Flask, MySQL, and Redis. I implemented persistent storage using Docker volumes and service communication through Docker networking. During development, I diagnosed and resolved issues such as MySQL authentication failures, missing tables, JSON serialization problems, and container startup errors using Docker logs, Docker Compose logs, and container inspection commands."

---

# Key Learning Outcomes

By completing this project, I gained hands-on experience with:

- Docker images
- Docker containers
- Dockerfile creation
- Docker Compose
- Docker networking
- Docker volumes
- Redis caching
- MySQL integration
- REST API deployment
-
