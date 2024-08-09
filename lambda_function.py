import json
import boto3
from boto3.dynamodb.conditions import Key

# DynamoDBへの接続を初期化
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    for message in event['Records']:
        process_message(message)
    print("done")

def process_message(message):
    try:
        data  = json.loads(message['body'])
        operation = data['operation']
        
        if (operation == "POST"):
            Item = {
                "email": data['Email'],
                "FirstName": data['FirstName'],
                "LastName" : data['LastName']
            }
            # DynamoDBにデータを登録
            response = table.put_item(
                Item = Item
            )
        else:
            raise ValueError('Unrecognized operation "{}"'.format(operation))
    except ClientError as err:
        print ("DB Client Error Reason: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
        )
        raise err
    except Exception as err:
        print("An error occurred")
        raise err
