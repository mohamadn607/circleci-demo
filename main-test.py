# Import the Add function, and assert that it works correctly.
from main import Multiply

def TestMultiply():
        assert Multiply(2,3) == 6
        assert Multiply(5,5) == 25
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()