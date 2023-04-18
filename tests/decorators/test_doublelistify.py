import unittest

from src.decorators import doublelistify


class TestBatchify(unittest.TestCase):

    def test_doublelistify(self):

        @doublelistify
        def square(items):
            return [item ** 2 for item in items]

        test_input = [list(range(3)) for _ in range(3)]
        expected = [[item ** 2 for item in items] for items in test_input]

        self.assertEqual(square(test_input), expected)


if __name__ == '__main__':
    unittest.main()
