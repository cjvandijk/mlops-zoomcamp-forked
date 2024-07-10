import json
import requests 
import os
from pprint import pprint
from deepdiff import DeepDiff

os.environ["AWS_PROFILE"] = "/home/ubuntu/.aws/credentials"

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49630081666084879290581185630324770398608704880802529282",
                "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDI1NgogICAgfQ==",
                "approximateArrivalTimestamp": 1654161514.132
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49630081666084879290581185630324770398608704880802529282",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::387546586013:role/lambda-kinesis-role",
            "awsRegion": "eu-west-1",
            "eventSourceARN": "arn:aws:kinesis:eu-west-1:387546586013:stream/ride_events"
        }
    ]
}


url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
actual_response = requests.post(url, json=event).json()
print("ACTUAL RESPONSE")
pprint(actual_response)

expected_response = {
    'predictions': [{
        'model': 'ride_duration_prediction_model', 
        'version': 'Test123', 
        'prediction': {
            'ride_duration': 18.2,
            'ride_id': 256
        }
    }]
}

diff = DeepDiff(actual_response, expected_response, significant_digits=1)

print("DIFFERENCE:")
pprint(diff)

# assert actual_response == expected_response
assert "values_changed" not in diff
# da8a85f0cfc94022891e42f77ed37298


