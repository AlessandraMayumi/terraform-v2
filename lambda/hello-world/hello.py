def lambda_handler(event, context):
    print('Event: ', event)
    message = 'Hello, World!'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body' : message
    }
