import requests
import json
import os

headers =  {
            "x-api-key":"8glGnQyqkOgqSTbQE2JFaEvEWJNJa6b6ZdUIpapb"
            }

api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/health"
response = requests.get(api_url, headers=headers)

print(response.json())
print(response.status_code)


api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/conversation"
todo = {"conversationId": "", 
        "message": { "content": [ { "contentType": "text",
                                    "mediaType": "", 
                                    "body": "Which University is the best in China?"} ],
                     "model": "claude-v3-sonnet"} 
        }



response = requests.post(api_url, data=json.dumps(todo), headers=headers)

print(response.json())
print(response.status_code)

conversationId = response.json().conversationId
messageId = response.json().messageId
api_url = "https://z82v57b3q1.execute-api.us-east-1.amazonaws.com/api/conversation/" + conversationId + "/" + messageId
response = requests.get(api_url, headers=headers)

print(response.json())
print(response.status_code)
