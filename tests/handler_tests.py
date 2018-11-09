import unittest

import main

class HandlerTests(unittest.TestCase):

    def test_assert(self):
        self.assertTrue(True)
    
    def test_handler_return_ok(self):
        self.assertEqual(main.handler(None, None), { 'ok': True })

if __name__ == '__main__':
    unittest.main()
