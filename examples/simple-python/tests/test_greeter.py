from src.greeter import greet


def test_greet():
    assert greet("Amir") == "Hello, Amir!"
