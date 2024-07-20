"""Testing"""


def add_numbers(x:int, y:int) -> int:
    """adds two numbers together"""
    return x + y


if __name__ == "__main__":
    g = add_numbers  # Turns out you can store function in a variable
    print(g(2, 3))
