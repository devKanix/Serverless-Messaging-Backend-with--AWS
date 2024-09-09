import boto3
import json

sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-south-1.amazonaws.com/417117090286/ChatAPP'

data = {
    'user_id': 123,
    'message': 'Hello! I am Kanishk Chaudhary and This is Serverless message transfer to the reciver person with the help of "SQS"',
    'timestamp': '2024-06-28T12:00:00Z'
}

message_body = json.dumps(data)

# Send a message to the queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message_body
)

print(f"MessageId: {response['MessageId']}")
