import unittest

from src.inference.double_list_inference import deflatten, flatten, inference_double_list


class TestFlatten(unittest.TestCase):

    def test(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(flatten(input), expected)


class TestDeflatten(unittest.TestCase):

    def test(self):
        test_cases = [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [3, 3, 3],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            ],  # case1
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 3, 5],
                [[1], [2, 3, 4], [5, 6, 7, 8, 9]],
            ],  # case2
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
                [[], [1], [2], [], [3], [4], [], [5], [6], [7], [8], [9]],
            ],  # case3
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(deflatten(case[0], case[1]), case[2])


class TestInferenceDoubleList(unittest.TestCase):

    def test(self):
        def inference_func(xs):
            return [x ** 2 for x in xs]

        test_cases = [
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 4, 9], [16, 25, 36], [49, 64, 81]],
            ],  # case1
            [
                [[1], [2, 3, 4], [5, 6, 7, 8, 9]],
                [[1], [4, 9, 16], [25, 36, 49, 64, 81]],
            ],  # case2
            [
                [[], [1], [2], [], [3], [4], [], [5], [6], [7], [8], [9]],
                [[], [1], [4], [], [9], [16], [], [25], [36], [49], [64], [81]],
            ],  # case3
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(inference_double_list(case[0], inference_func), case[1])


if __name__ == '__main__':
    unittest.main()
