import unittest
from unittest import mock
from test_complex import Test, new_test, func


class TestingTestClass(unittest.TestCase):

    def setUp(self):
        self.test = Test()
        print('You can test func')

    def tearDown(self):
        print('Exit from test func')

    def test_enter(self):
        self.assertEqual(self.test.__enter__(), self.test)

    @mock.patch('test_complex.Test.__exit__', mock.Mock(return_value=True))
    def test_exit(self):
        self.assertEqual(self.test.__exit__(1, 1, 1), True)

    def test_hello(self):
        self.assertEqual(func(), 1)

    def test_new_test(self):
        self.assertIsInstance(new_test(), Test)


if __name__ == '__main__':
    unittest.main()
