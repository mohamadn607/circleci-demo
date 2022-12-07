# Import the Add function, and assert that it works correctly.
from main import Multiply

def TestMultiply():
        assert Multiply(2,4) == 8
        assert Multiply(5,6) == 30
        print("Multiply Function works correctly")

if __name__ == '__main__':
        TestMultiply()