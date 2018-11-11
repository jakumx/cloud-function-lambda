import unittest
import os
from lib.mysql import Mysql

class BaseTest(unittest.TestCase):

    def setUp(self):
        Mysql().create_by_script('seed.sql')