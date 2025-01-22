# employees-directory-app
A Flask-based employee directory where employees can input their details (name, position, badges, and picture). The picture is stored in AWS S3, while other details are stored in AWS DynamoDB. After submission, the employee's profile is displayed.


## Features
✔️ Web-based form for employee input
✔️ Stores images in AWS S3
✔️ Stores employee details in AWS DynamoDB
✔️ Displays employee profiles dynamically
✔️ Deployable to AWS EC2 with user data

## Technologies Used
Python Flask (Backend)
AWS S3 (Image Storage)
AWS DynamoDB (Database)
HTML & CSS (Frontend)
Boto3 (AWS SDK for Python)

## Setup & Installation
1. Clone the Repository
```
git clone https://github.com/your-username/employee-directory.git
cd employee-directory
```

2. Install Dependencies
```
pip install -r requirements.txt
```

3. Set Up AWS Credentials
Ensure your AWS CLI is configured with an IAM user having S3 & DynamoDB access:

```
aws configure
```

Or, set environment variables:

```
export AWS_REGION="us-east-1"
export S3_BUCKET="your-s3-bucket-name"
export DYNAMO_TABLE="your-dynamodb-table-name"
```

4. Run the Flask App
```
python app.py
```
Visit http://127.0.0.1:5000 in your browser.

## Deployment to AWS EC2
Launch an EC2 instance (Amazon Linux 2).
Attach an IAM role with S3 & DynamoDB permissions.

Use the following user data script to deploy automatically:
```
#!/bin/bash
sudo yum update -y
sudo yum install -y python3 python3-pip git aws-cli
cd /home/ec2-user
git clone https://github.com/your-username/employee-directory.git
cd employee-directory
pip3 install -r requirements.txt
export AWS_REGION="us-east-1"
export S3_BUCKET="your-s3-bucket-name"
export DYNAMO_TABLE="your-dynamodb-table-name"
python3 app.py > app.log 2>&1 &
echo "@reboot python3 /home/ec2-user/employee-directory/app.py > /home/ec2-user/employee-directory/app.log 2>&1 &" | crontab -
```

Open EC2 public IP in browser:
http://<ec2-public-ip>:5000

## Usage
Fill out the employee form.
Upload a profile picture.
Click Submit.
View the employee profile.

