import requests

class Blog:

    def posts():
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()

    def post_by_user_id(userId: str):
        e = f"https://jsonplaceholder.typicode.com/posts/{userId}"
        response = requests.get(e)
        return response.json()
    
data = Blog.posts()

data_by_id = Blog.post_by_user_id("6")

# print(data[0])
print(data_by_id)