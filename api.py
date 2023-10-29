import json

def lambda_handler(event, context):
    # Check if the path parameter 'id' is present in the event
    if 'id' in event['pathParameters']:
        # Handle requests for /{id}
        id = event['pathParameters']['id']
        response = {
            "statusCode": 200,
            "body": json.dumps(f"Received request for ID: {id}")
        }
    else:
        # Handle requests for /
        response = {
            "statusCode": 200,
            "body": json.dumps("Received request for the root path")
        }

    return response
