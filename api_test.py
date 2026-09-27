import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

new_data = {
    "user_id": 1,
    "title": "polundra",
    "completed": False,
}
response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_data)
print(response.status_code)
print(response.json())
