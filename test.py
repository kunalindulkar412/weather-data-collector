import requests

info ={
    "userId": 1,
    "id": 5
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=info)

# print(response)
# print(response.url)
# print(response.text)
# print(response.json())

output = response.json()[0]
userId = output['userId']
post_id = output['id']
title = output['title']
body = output['body']
print(f"userId: {userId} \nid: {post_id} \ntitle: {title} \nbody: {body}")