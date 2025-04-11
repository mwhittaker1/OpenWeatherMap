from main import lambda_handler

event = {
    "queryStringParameters": {
        "zip": "08043"
    }
}
context = {}

response = lambda_handler(event, context)
print("Response:")
print(response)
