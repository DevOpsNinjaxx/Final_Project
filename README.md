# Django AWS RDS Connection Checker

This is a Django application that allows you to check the connection status to an AWS RDS instance and view a history of connection statuses.

## Prerequisites

Before setting up and running the application, make sure you have the following installed:

- Python
- Django

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-aws-rds-connection-checker.git
cd django-aws-rds-connection-checker
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Create an AWS RDS Instance
a. Sign in to the AWS Management Console
Visit AWS Management Console and sign in to your AWS account.

b. Navigate to RDS
Navigate to the Amazon RDS service by searching for "RDS" in the AWS Management Console.

c. Launch a New RDS Instance
Click on "Create database" to launch a new RDS instance.

d. Configure Database Settings
Choose the database creation method (Standard Create).
Select the engine type (e.g., MySQL).
Configure settings such as DB instance identifier, master username, master password, and other options.
e. Configure Advanced Settings
Configure additional settings like VPC, Subnet Group, and security group. Make sure to set the publicly accessible option if your Django application needs to connect from outside the VPC.

f. Create Database
Click on "Create database" to launch the RDS instance. Wait for the instance to be created.

4. Configure Django Settings
Edit the settings.py file in the dbconnect app to configure the AWS RDS connection. Update the DATABASES setting with your RDS details:

# dbconnect/settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_rds_endpoint',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

```
Replace your_db_name, your_db_user, your_db_password, and your_rds_endpoint with the details from your RDS instance.

### 5. Apply Migrations
Run the Django migrations to set up the database:

```bash
python manage.py migrate
```

### 6. Run the Application
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/check_rds in your browser to access the application.
