# Application Deployment

## 1. Backend EC2

```bash
sudo yum update -y
sudo yum install python3 -y

git clone <YOUR_REPOSITORY_URL>
cd AWS-Three-Tier-Web-Application-Project/backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export DB_HOST="YOUR_RDS_ENDPOINT"
export DB_USER="YOUR_DB_USER"
export DB_PASSWORD="YOUR_DB_PASSWORD"
export DB_NAME="dev"

python app.py
```

The Flask API listens on:

```text
0.0.0.0:5000
```

## 2. Frontend EC2

```bash
sudo yum install nginx -y

sudo cp frontend/index.html /usr/share/nginx/html/index.html
sudo cp frontend/proxy.conf /etc/nginx/conf.d/reverse-proxy.conf

sudo nginx -t
sudo systemctl enable nginx
sudo systemctl restart nginx
```

## 3. AWS Request Flow

```text
Route 53 / Public Domain
        │
        ▼
Frontend ALB
        │
        ▼
Frontend EC2 + Nginx
        │
        │ /users
        ▼
Backend ALB / Backend EC2
        │
        ▼
Flask Application
        │
        ▼
Amazon RDS MySQL
```

## 4. Security Groups

Recommended traffic flow:

- Internet → Frontend ALB: HTTP/HTTPS
- Frontend ALB → Frontend EC2: HTTP
- Frontend EC2 → Backend ALB/backend: application traffic
- Backend → RDS: TCP 3306
- RDS should not be open to the public Internet.

Use the actual security-group rules from your deployment.
