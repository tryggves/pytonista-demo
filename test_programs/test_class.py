# content of test_class.py
class TestClass:
    num = 1

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        x = "check"
        assert hasattr(x, "check")

    def test_four(self):
        assert hasattr(self, "num")
