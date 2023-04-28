import unittest
import time
from app_sqlite import get_books_db_all
import argparse
import pytest

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


class TestSum():
    def __init__(self, count, timer):
        self.count = count
        self.timer = timer

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        sums  = 0
        for i in range(self.count+1):
            sums += i
            time.sleep(self.timer)
        print("sums {}".format(sums))
        assert sums == (self.count*(self.count+1))/(2)
        # self.assertEqual(sums, (self.n*(self.n+1))/(2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
    parser.add_argument('-c', '--count')# option that takes a value
    parser.add_argument('-t', '--timer')# option that takes a value
    args = parser.parse_args()

    test  = TestSum(int(args.count), float(args.timer))
    test.test_list_int()
