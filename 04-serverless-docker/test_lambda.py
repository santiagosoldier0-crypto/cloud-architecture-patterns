import json

from lambda_function import handler


def test_lambda_handler():
    result = handler({"queryStringParameters": {"name": "Ada"}}, None)
    assert result["statusCode"] == 200
    assert json.loads(result["body"]) == {"message": "hello Ada"}
