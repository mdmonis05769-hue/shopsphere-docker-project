# 📡 ShopSphere API Documentation

## Overview

ShopSphere provides REST APIs for accessing product information.

The API is built using **Flask** and returns responses in **JSON** format.

Base URL

```
http://localhost:5000
```

---

# API List

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home API |
| GET | /health | Health Check |
| GET | /products | Get Products |

---

# 1. Home API

## Endpoint

```
GET /
```

Purpose

Returns application information.

---

### Request

```
GET http://localhost:5000/
```

---

### Success Response

```json
{
    "application":"ShopSphere API",
    "version":"3.0",
    "message":"MySQL + Redis"
}
```

---

### Status Code

```
200 OK
```

---

# 2. Health API

## Endpoint

```
GET /health
```

Purpose

Checks whether the backend service is running correctly.

---

### Request

```
GET http://localhost:5000/health
```

---

### Response

```json
{
    "status":"Healthy"
}
```

---

### Status Code

```
200 OK
```

---

# 3. Products API

## Endpoint

```
GET /products
```

Purpose

Returns all available products stored in the MySQL database.

If Redis already contains cached data, the response is served from Redis.

---

### Request

```
GET http://localhost:5000/products
```

---

### Success Response

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
  },
  {
    "id":3,
    "name":"Gaming Mouse",
    "price":2200
  },
  {
    "id":4,
    "name":"Monitor",
    "price":18000
  },
  {
    "id":5,
    "name":"Headphones",
    "price":3500
  }
]
```

---

### Status Code

```
200 OK
```

---

# Response Format

Every successful API returns JSON.

Example

```json
{
    "key":"value"
}
```

or

```json
[
    {
        "id":1
    }
]
```

---

# HTTP Status Codes

| Code | Meaning |
|------|----------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# Error Example

If an API endpoint does not exist.

Request

```
GET /users
```

Response

```html
404 Not Found
```

---

# Testing Using Browser

Open

```
http://localhost:5000/
```

---

Open

```
http://localhost:5000/health
```

---

Open

```
http://localhost:5000/products
```

---

# Testing Using curl

Home

```bash
curl http://localhost:5000/
```

---

Health

```bash
curl http://localhost:5000/health
```

---

Products

```bash
curl http://localhost:5000/products
```

---

# Expected curl Output

```json
{
    "application":"ShopSphere API",
    "version":"3.0",
    "message":"MySQL + Redis"
}
```

---

# Testing Using Postman

Method

```
GET
```

URL

```
http://localhost:5000/products
```

Click

```
Send
```

Expected

```
200 OK
```

JSON Response

---

# API Request Lifecycle

```
Browser

↓

Flask API

↓

Redis Cache

↓

Cache Hit?

↓

Yes

↓

Return Response

↓

No

↓

MySQL Query

↓

JSON Response

↓

Save in Redis

↓

Return Client
```

---

# Cache Behaviour

### First Request

```
Browser

↓

MySQL

↓

Redis

↓

Browser
```

---

### Second Request

```
Browser

↓

Redis

↓

Browser
```

No database query is executed.

---

# API Performance

Without Redis

```
Client

↓

Backend

↓

MySQL

↓

Backend

↓

Client
```

---

With Redis

```
Client

↓

Backend

↓

Redis

↓

Client
```

This reduces database load and improves response time.

---

# Security Improvements (Future)

Current API is open.

Future enhancements can include:

- JWT Authentication
- OAuth2
- API Keys
- HTTPS
- Rate Limiting
- Input Validation
- Logging
- Request Monitoring

---

# Future API Endpoints

```
POST /products

PUT /products/{id}

DELETE /products/{id}

POST /login

POST /register

GET /orders

POST /orders

GET /users
```

---

# API Best Practices Followed

- RESTful endpoints
- JSON responses
- Proper HTTP status codes
- Separation of concerns
- Database abstraction
- Redis caching
- Dockerized deployment
- Simple endpoint structure
- Easy testing
- Production-ready architecture

---

# Summary

This API demonstrates:

- Flask REST API development
- MySQL integration
- Redis caching
- Docker Compose deployment
- JSON responses
- REST architecture
- Production debugging
- Multi-container communication
