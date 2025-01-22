from flask import Flask, render_template, request, redirect, url_for
import boto3
import uuid

app = Flask(__name__)

# AWS Configuration
S3_BUCKET = 'employee-app-dir-ha-401'
DYNAMO_TABLE = 'Employees'

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMO_TABLE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form['name']
    position = request.form['position']
    picture = request.files['picture']

    # Generate unique file name and upload picture to S3
    picture_key = f"{uuid.uuid4()}-{picture.filename}"
    s3_client.upload_fileobj(picture, S3_BUCKET, picture_key)
    picture_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{picture_key}"

    # Store employee details in DynamoDB
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'name': name,
        'position': position,
        'picture_url': picture_url
    })

    return redirect(url_for('profile', name=name))

@app.route('/profile/<name>')
def profile(name):
    # Retrieve employee details from DynamoDB
    response = table.scan(FilterExpression=boto3.dynamodb.conditions.Attr('name').eq(name))
    if response['Items']:
        employee = response['Items'][0]
    else:
        return "Employee not found", 404

    return render_template('profile.html', employee=employee)

if __name__ == '__main__':
    app.run(debug=True)