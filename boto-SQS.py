#### SQS producer #####
import boto3

# Replace 'your-queue-url' with your actual SQS queue URL
sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/your-account-id/your-queue-name'

def lambda_handler(event, context):
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    # Send a message to the SQS queue
    message_body = "Hello, SQS!"
    response = sqs.send_message(
        QueueUrl=sqs_queue_url,
        MessageBody=message_body
    )

    # Log the message ID for reference
    print(f"Message sent with ID: {response['MessageId']}")
    
    return {
        'statusCode': 200,
        'body': 'Message sent to SQS successfully.'
    }

#### SQS consumer ####import boto3

# Replace 'your-queue-url' with your actual SQS queue URL
sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/your-account-id/your-queue-name'

def lambda_handler(event, context):
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    # Receive messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=sqs_queue_url,
        MaxNumberOfMessages=1,  # Adjust as needed
        WaitTimeSeconds=20      # Adjust as needed
    )

    # Check if there are messages in the response
    if 'Messages' in response:
        for message in response['Messages']:
            # Process the message
            message_body = message['Body']
            print(f"Received message: {message_body}")

            # Delete the message from the queue to prevent reprocessing
            receipt_handle = message['ReceiptHandle']
            sqs.delete_message(QueueUrl=sqs_queue_url, ReceiptHandle=receipt_handle)
    else:
        print("No messages in the queue")

    return {
        'statusCode': 200,
        'body': 'SQS messages consumed successfully.'
    }

