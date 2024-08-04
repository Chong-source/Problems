"""Testing"""
import numpy as np

def add_numbers(x:int, y:int) -> int:
    """adds two numbers together"""
    return x + y

def add_one(x):
    return x + 1


if __name__ == "__main__":
    g = add_numbers  # Turns out you can store function in a variable
    print(g(2, 3))
    a = np.array([[1, 1, 1],
                  [1, 1, 1]])
    b = np.array([[1, 1, 1],
                  [1, 2, 1],
                  [1, 1, 1]])
    print(a @ b)
    print(add_one(a))
