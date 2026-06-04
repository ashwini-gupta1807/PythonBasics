import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
}

response = requests.post(url, json = data, headers = headers)

print(response.status_code)
print(response.json())