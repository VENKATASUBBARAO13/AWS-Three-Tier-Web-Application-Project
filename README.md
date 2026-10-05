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

![UserFlow Dashboard](screenshots/01-userflow-dashboard.png)

### User Update

![User Update](screenshots/02-user-update.png)

### User Delete

![User Delete](screenshots/03-user-delete.png)

### Application After Delete

![Application After Delete](screenshots/04-application-after-delete.png)

### Amazon RDS MySQL

![Amazon RDS MySQL](screenshots/05-rds-mysql.png)

### Amazon EC2 Instances

![Amazon EC2 Instances](screenshots/06-ec2-instances.png)

### Application Load Balancers

![Application Load Balancers](screenshots/07-application-load-balancers.png)

### Application Through Load Balancer

![Application Through ALB](screenshots/08-application-through-alb.png)

### Application Through Custom Domain

![Application Through Custom Domain](screenshots/09-application-custom-domain.png)

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
