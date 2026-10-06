# AWS Three-Tier Web Application Deployment

A hands-on AWS project demonstrating the deployment of a web application using a three-tier architecture:

- **Presentation Tier** — Frontend application
- **Application Tier** — Backend application
- **Data Tier** — Amazon RDS MySQL database

The application was deployed on Amazon EC2 and exposed through Application Load Balancers, with the backend connected to an Amazon RDS MySQL database.

## 🏗️ Architecture

```text
                         Users
                           |
                           v
                    Application Load Balancer
                           |
              +------------+------------+
              |                         |
              v                         v
        Frontend EC2              Backend EC2
       (Presentation)            (Application)
                                      |
                                      v
                              Amazon RDS MySQL
                                (Data Tier)
```

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| **Amazon VPC** | Provides the isolated networking environment |
| **Amazon EC2** | Hosts the frontend and backend applications |
| **Application Load Balancer** | Distributes incoming application traffic |
| **Amazon RDS** | Hosts the MySQL database |
| **Security Groups** | Controls network access between resources |
| **Route 53 / Custom Domain** | Provides domain-based access to the application |
| **IAM** | Provides controlled access to AWS resources |

## 📐 Three-Tier Design

### 1. Presentation Tier

The frontend application is deployed on an EC2 instance and provides the user-facing interface.

### 2. Application Tier

The backend application runs on a separate EC2 instance and handles application logic and database communication.

### 3. Data Tier

Amazon RDS for MySQL is used as the managed database layer. The database is accessed by the backend application rather than directly by end users.

## 🔄 Application Flow

```text
User
  |
  v
Frontend / Application Load Balancer
  |
  v
Frontend EC2
  |
  v
Backend / Application Load Balancer
  |
  v
Backend EC2
  |
  v
Amazon RDS MySQL
```

## 🚀 Deployment Highlights

- Deployed frontend and backend components on separate EC2 instances.
- Configured Application Load Balancers for application traffic.
- Connected the backend application to Amazon RDS MySQL.
- Verified EC2 instances were running successfully.
- Verified the RDS database was available.
- Tested application operations such as adding, updating, and deleting users.
- Accessed the deployed application through a custom domain.

## 🧪 Application Testing

The deployed **UserFlow** application was tested with CRUD operations:

- Add user
- Update user
- Delete user
- Display total users
- Display active users
- Display email accounts
- Search users

The screenshots demonstrate successful application operations and database-backed user management.

## 📸 Screenshots

> The screenshots below document the deployed application and AWS infrastructure.

### Application Dashboard

![UserFlow Dashboard](screenshots/userflow-dashboard.png)

### User Update

![User Update](screenshots/user-update.png)

### User Delete

![User Delete](screenshots/user-delete.png)

### Application After Delete

![Application After Delete](screenshots/user-added-successfully.png)

### Amazon RDS MySQL

![Amazon RDS MySQL](screenshots/rds-mysql.png)

### Amazon EC2 Instances

![Amazon EC2 Instances](screenshots/ec2-instances.png)

### Application Load Balancers

![Application Load Balancers](screenshots/application-load-balancers.png)

### Application Through Load Balancer

![Application Through ALB](screenshots/application-through-alb.png)

### Application Through Custom Domain

![Application Through Custom Domain](screenshots/application-custom-domain.png)

## 💻 Application Source Code

The repository now includes the application source code used for the three-tier deployment.

### Backend — Flask REST API

Location:

```text
backend/
├── app.py
├── requirements.txt
├── test.sql
└── README.md
```

The backend provides CRUD APIs for the `users` table in Amazon RDS MySQL.

### Backend API

```python
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users ORDER BY id")
        return jsonify(cursor.fetchall())
    finally:
        cursor.close()
        conn.close()


@app.route("/users/add", methods=["POST"])
def add_user():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        return jsonify({"message": "User added successfully"}), 201
    finally:
        cursor.close()
        conn.close()
```

Additional endpoints implemented in `backend/app.py`:

```text
GET    /users/<id>
PUT    /users/update/<id>
DELETE /users/delete/<id>
```

### MySQL Database

The database schema is available in `backend/test.sql`:

```sql
CREATE DATABASE IF NOT EXISTS dev;
USE dev;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

### Frontend — HTML / CSS / JavaScript

Location:

```text
frontend/
├── index.html
├── proxy.conf
├── proxy-process.md
└── README.md
```

The frontend provides:

- User listing
- Add user
- Update user
- Delete user
- Total users
- Active users
- Email account count

Example frontend API call:

```javascript
const API_BASE = "";

fetch(API_BASE + "/users")
  .then(response => response.json())
  .then(users => {
      console.log(users);
  });
```

### Nginx Reverse Proxy

The frontend uses Nginx to serve the web application and forward API requests to the backend.

```nginx
server {
    listen 80;
    server_name _;

    location /users {
        proxy_pass http://BACKEND_PRIVATE_IP:5000;
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

Replace `BACKEND_PRIVATE_IP` with the backend EC2 private address or the internal backend load-balancer DNS name used in the deployment.

## 🔄 Application Request Flow

```text
User
 │
 ▼
Route 53 / Custom Domain
 │
 ▼
Frontend ALB
 │
 ▼
Frontend EC2
 │
 ▼
Nginx
 │
 ├── /          → Frontend index.html
 │
 └── /users     → Backend ALB / Backend EC2
                     │
                     ▼
                Flask REST API
                     │
                     ▼
                Amazon RDS MySQL
```

## 📂 Repository Structure

```text
AWS-Three-Tier-Web-Application-Project/
│
├── README.md
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── test.sql
│   └── README.md
│
├── frontend/
│   ├── index.html
│   ├── proxy.conf
│   ├── proxy-process.md
│   └── README.md
│
├── deployment/
│   └── README.md
│
└── screenshots/
    ├── userflow-dashboard.png
    ├── user-update.png
    ├── user-delete.png
    ├── user-added-successfully.png
    ├── rds-mysql.png
    ├── ec2-instances.png
    ├── application-load-balancers.png
    ├── application-through-alb.png
    └── application-custom-domain.png
```

> The application credentials in the repository are placeholders. Use environment variables or deployment configuration for real database credentials.

## 🎯 Key Learning Outcomes

- Understanding AWS three-tier application architecture
- Deploying applications on Amazon EC2
- Working with Application Load Balancers
- Connecting an application server to Amazon RDS MySQL
- Configuring AWS networking and security controls
- Testing application availability through load-balanced endpoints
- Troubleshooting and validating a cloud-hosted application

## ⚠️ Security & Cost Note

This project was created for hands-on learning and demonstration purposes. AWS resources such as EC2 instances, load balancers, and RDS databases can incur charges. Resources should be stopped or deleted when they are no longer required.

---

**Project:** AWS Three-Tier Web Application Deployment  
**Application:** UserFlow  
**Cloud Platform:** Amazon Web Services (AWS)
