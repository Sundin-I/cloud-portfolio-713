import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoItems')

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'POST':
        data = json.loads(event['body'])
        item = {
            'id': str(uuid.uuid4()),
            'task': data['task']
        }
        table.put_item(Item=item)
        return respond(200, item)
    
    elif method == 'GET':
        items = table.scan()['Items']
        return respond(200, items)
    
    else:
        return respond(405, {'error': 'Method Not Allowed'})

def respond(status, body):
    return {
        'statusCode': status,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(body)
    }
