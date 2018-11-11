import unittest
import main
import main_lambda
import json
from tests.base import BaseTest

class HandlerTests(BaseTest):
    
    def test_main_handler(self):
        handler_response = main.handler(None)

        self.assertIsInstance(handler_response, bytes)
        response = json.loads(handler_response)

        self.assertIn('personaje', response)
        self.assertIn('frase', response)

    def test_main_lambda_hanlder(self):
        handler_response = main_lambda.handler(None, None)

        self.assertIn('name', handler_response)
        self.assertIn('quote', handler_response)

if __name__ == '__main__':
    unittest.main()
