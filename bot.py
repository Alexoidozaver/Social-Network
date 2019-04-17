import faker
import requests
import json
import random

user_amount = 3
max_posts_per_user = 4
max_likes_per_user = 2

users = []
fake = faker.Faker()
while user_amount:
    data = {
            "username": fake.name(),
            "password": fake.password(length=10),
            "email": fake.email()
    }
    headers = {
        'Content-Type': 'application/json',
    }
    result = requests.post('http://127.0.0.1:5000/user/registration', data=json.dumps(data), headers=headers)
    if result.status_code == 201:
        access_token = json.loads(result.text)["access_token"]
        data["access_token"] = access_token
        users.append(data)
        user_amount -= 1
        print(result.__dict__)

# creating posts
posts_ids = []
for user in users:
    for i in range(random.randint(0, max_posts_per_user)):
        data = {
            "text": fake.text(),
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + user["access_token"]
        }
        result = requests.post('http://127.0.0.1:5000/post', data=json.dumps(data), headers=headers)
        post_id = json.loads(result.text)[0]["id"]
        posts_ids.append(post_id)
        print(result.__dict__)

# random creating likes(may be slow or stop if likes per user is too big compared to all posts amount)
print(posts_ids)
for user in users:
    likes_amount = random.randint(0, max_likes_per_user)
    while likes_amount:
        data = {
            "post_id": random.choice(posts_ids)
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + user["access_token"]
        }
        result = requests.post('http://127.0.0.1:5000/like', data=json.dumps(data), headers=headers)
        if result.status_code == 200:
            likes_amount -= 1
            print(result.__dict__)
