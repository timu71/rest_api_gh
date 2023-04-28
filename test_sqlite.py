import unittest

from app_sqlite import get_books_db_all

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
class TestSql(unittest.TestCase):
    def test_database(self):
        """
        Test that it can sum a list of integers
        """
        books = get_books_db_all()
        print(len(books))
        self.assertEqual(len(books), 30)

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
