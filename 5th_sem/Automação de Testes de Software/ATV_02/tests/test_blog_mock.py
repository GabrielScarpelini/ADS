import pytest
from unittest.mock import Mock

@pytest.fixture
def posts():
    posts = [{"userid": 11, "id": 11, "title": "Test Automation Using Fixture N Mock", "body": "Mock is like and Dublê that you put a cot do pretend its the actual data base..." },
             {"userid": 21, "id": 21, "title": "How to Create a Pytest Modute", "body": "The pytest.ini is very important to run the by pytest in it's folder by the terminal..."}]
    return posts
    
@pytest.fixture
def post_by_user_id():
    post = [{"userid": 21, "id": 21, "title": "How to Create a Pytest Modute", "body": "The pytest.ini is very important to run the by pytest in it's folder by the terminal..."}]
    return post

def test_blog_data(posts):
    blog = Mock()
    blog.posts.return_value = posts
    result = blog
    assert result != None

def test_src_by_id(post_by_user_id):
    blog = Mock()
    blog.get_by_id.return_value = post_by_user_id
    result = blog.get_by_id(21)
    assert result != None