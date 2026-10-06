# Backend

Flask REST API for the Application Tier.

## API Endpoints

```text
GET    /users
GET    /users/<id>
POST   /users/add
PUT    /users/update/<id>
DELETE /users/delete/<id>
```

## Run

```bash
sudo yum install python3 -y

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export DB_HOST="YOUR_RDS_ENDPOINT"
export DB_USER="YOUR_DB_USER"
export DB_PASSWORD="YOUR_DB_PASSWORD"
export DB_NAME="dev"

python app.py
```

The API listens on port `5000`.
