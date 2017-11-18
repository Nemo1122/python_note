import unittest


class A:
    x = 50

    def __init__(self):
        self.a = 5
        self.b = 10

    def add(self):
        print(self.a + self.b)

    def add2(self):
        print(self.x + 100)


class B(A):
    def add3(self):
        self.add()


class BA(B):
    def test_b(self):
        self.add3()


class TestBA(unittest.TestCase, B):
    def test_b(self):
        self.add3()


# ba = BA()
# ba.test_b()
if __name__ == '__main__':
    unittest.main()