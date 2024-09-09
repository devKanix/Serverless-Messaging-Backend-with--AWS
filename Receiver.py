import boto3
import json

sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-south-1.amazonaws.com/417117090286/ChatAPP'

while True:
    print("Retrieving messages")
    
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20,
    )
    if "Messages" in response:
        for message in response["Messages"]:
            try:
                message_body = json.loads(message['Body'])
                print(f"Message body: {message_body}")
                
                user_id = message_body['user_id']
                message_text = message_body['message']
                timestamp = message_body['timestamp']
                
                print(f"Message: {message_text}")
                
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Removed message: {message['MessageId']}")
                
            except json.JSONDecodeError as e:
                print(f"Error parsing message JSON: {e}")
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Removed invalid message: {message['MessageId']}")
    
    else:
        print("No messages received")

    import time
    time.sleep(5)
