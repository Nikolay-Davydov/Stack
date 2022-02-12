import unittest
from Stack import check_balance

class TestUnitTestMain(unittest.TestCase):
    def setUp(self):
       print("method setUp")

    def tearDown(self):
        print("method teardown")

    @classmethod
    def setUpClass(cls):
        print("method setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("method tearDownClass")

    def test_check_balance(self):
        self.assertEqual(check_balance('{{[()]}}'), "Сбалансировано")
        self.assertEqual(check_balance('{{[(])]}}'), "Несбалансировано")