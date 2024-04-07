import requests
import json
import os


REGION = os.environ.get("REGION", "ap-northeast-1")
print(REGION)

headers =  {
            "x-api-key":"8glGnQyqkOgqSTbQE2JFaEvEWJNJa6b6ZdUIpapb"
            }

api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/health"
response = requests.get(api_url, headers=headers)

print(response.json())
print(response.status_code)


api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/conversation"
todo = {"conversationId": "dpliu", 
        "message": { "content": [ { "contentType": "text",
                                    "mediaType": "", 
                                    "body": "Which University is the best in China?"} ],
                     "model": "claude-v3-sonnet"} 
        }



response = requests.post(api_url, data=json.dumps(todo), headers=headers)

print(response.json())
print(response.status_code)



api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/conversation/dpliu/01HTVQH6R0Y2WWCJ1FPHBQS5X5"
response = requests.get(api_url, headers=headers)

print(response.json())
print(response.status_code)
