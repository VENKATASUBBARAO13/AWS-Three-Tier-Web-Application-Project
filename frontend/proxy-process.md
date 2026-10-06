# Frontend → Backend Communication Using Nginx

## Architecture

```text
User
 │
 ▼
Frontend ALB
 │
 ▼
Frontend EC2
 │
 ▼
Nginx
 ├── /       → index.html
 └── /users  → Backend EC2:5000
                  │
                  ▼
             Amazon RDS MySQL
```

## Request Flow

1. The browser requests the frontend.
2. Nginx serves `index.html`.
3. JavaScript calls `/users`.
4. Nginx matches `location /users`.
5. Nginx forwards the request to the backend private IP.
6. Flask processes the request.
7. Flask reads or updates Amazon RDS MySQL.
8. The JSON response returns through Nginx to the browser.

## Why Use Nginx?

- Keeps the backend application behind the frontend layer.
- Provides one public endpoint.
- Avoids exposing Flask port 5000 directly to users.
- Makes HTTPS/ALB integration easier.
- Centralizes frontend and API routing.

Replace `BACKEND_PRIVATE_IP` with your backend EC2 private IP or an internal load balancer DNS name.
