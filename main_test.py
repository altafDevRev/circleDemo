# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        assert Add(8,6) == 14
        assert Add(10,10) == 20
        print("Add Function works correctly")
        print("Add Function also works")

if __name__ == '__main__':
        TestAdd()
