import unittest, myutils


# subject method to test
def sum_of_nums(s: str) -> float:
    if s is None: 
        return None

    nums = [myutils.to_float(n) for n in s.split(',')]
    nums = [n for n in nums if n is not None]
    return sum(nums)


class TestSumOfNums(unittest.TestCase):
    def test_for_none_input(self):
        want = None
        got = sum_of_nums(None)
        self.assertEqual(want, got)

    def test_for_valid_input_with_numbers(self):
        want = 10.0
        got = sum_of_nums("1,vinod,kumar,9")
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
