import json


def handler(event, context):
    """AWS Lambda Python handler; returns an API Gateway proxy response."""
    name = event.get("queryStringParameters", {}).get("name", "world") if event.get("queryStringParameters") else "world"
    return {"statusCode": 200, "headers": {"content-type": "application/json"},
            "body": json.dumps({"message": f"hello {name}"})}
