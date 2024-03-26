import pytest
from src.blog import Blog

@pytest.fixture
def dados():
    return Blog.posts()

@pytest.fixture
def by_id():
    return Blog.post_by_user_id("6")

def test_blog_data(dados):
    assert len(dados) > 0

def test_by_id(by_id):
    assert by_id["title"] == "dolorem eum magni eos aperiam quia"
