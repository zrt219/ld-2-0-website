# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import importlib.util

TOKEN = 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC'
ctx = ssl._create_unverified_context()

post_id = "6ab1f1956ed20e9354f5d8ba"

spec = importlib.util.spec_from_file_location("biz", "scripts/schedule-juju-business-campaign.py")
biz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(biz)

post20 = biz.posts_data[19]

mutation = """
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
      }
    }
    ... on InvalidInputError {
      message
    }
    ... on LimitReachedError {
      message
    }
    ... on UnexpectedError {
      message
    }
    ... on NotFoundError {
      message
    }
  }
}
"""

variables = {
    "input": {
        "id": post_id,
        "dueAt": "2026-10-22T21:45:00.000Z",
        "schedulingType": "automatic",
        "mode": "customScheduled",
        "text": post20["text"],
        "assets": [
            {
                "image": {
                    "url": post20["assetUrl"]
                }
            }
        ]
    }
}

req = urllib.request.Request(
    'https://api.buffer.com',
    data=json.dumps({'query': mutation, 'variables': variables}).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
)

with urllib.request.urlopen(req, context=ctx) as r:
    data = json.loads(r.read().decode('utf-8'))
    print(json.dumps(data, indent=2))
