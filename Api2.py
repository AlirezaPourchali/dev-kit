import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'YourDynamoDBTableName'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    path_parameters = event.get('pathParameters', {})
    
    if event['httpMethod'] == 'GET':
        if not path_parameters:
            # Handle the / endpoint, list all items
            response = table.scan()
        else:
            # Handle the /{id} endpoint, get the item by user_id
            user_id = path_parameters['id']
            response = table.get_item(Key={'user_id': user_id})

        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item') if 'Item' in response else response.get('Items', []))
        }

    return {
        'statusCode': 400,
        'body': json.dumps('Bad Request')
    }
