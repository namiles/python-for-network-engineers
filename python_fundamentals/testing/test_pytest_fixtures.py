# def test_some_text():
#     with open("myinfo.txt") as f:
#         content = f.read()
#     assert "Tiger" in content

# If we want test against the contents of the my_info file we can use fixtures, 
# which enables the use of the decorated function in many tests

import pytest

@pytest.fixture
def my_info():
    with open("myinfo.txt") as f:
        content = f.read()
    return content

def test_one(my_info):
    assert "Tiger" in my_info
    assert "zebra" in my_info

def test_two(my_info):
    assert "lion" in my_info