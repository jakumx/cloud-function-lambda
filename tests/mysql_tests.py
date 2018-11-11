import unittest

from tests.base import BaseTest
from lib.mysql import Mysql


class MysqlTests(BaseTest):

    def test_randow_row(self):
        response = Mysql().random_row()

        self.assertIn('name', response)
        self.assertIn('quote', response)

if __name__ == '__main__':
    unittest.main()
