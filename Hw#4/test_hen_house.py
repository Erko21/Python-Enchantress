import unittest

from unittest import mock
from unittest.mock import patch
from hen_class import HenHouse


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.house = HenHouse(10)

    def test_wrong_hen_count(self):
        self.assertRaises(ValueError, HenHouse(6))

    def test_wrong_hen_count_else(self):
        self.assertEqual(self.house.__init__(6), None)

    def test_season(self):
        with patch('hen_class.datetime.datetime') as a:
            a.today().month = 7
            self.assertEqual(self.house.season, 'summer')

    @patch('hen_class.HenHouse._productivity_index', mock.Mock(return_value=1))
    def test_get_eggs_daily(self):
        self.assertEqual(self.house.get_eggs_daily(5), 5)

    @patch('hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup(self):
        self.assertEqual(self.house.get_max_count_for_soup(1), 9)

    @patch('hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup_zero(self):
        self.assertEqual(self.house.get_max_count_for_soup(15), 0)

    def test_food_price(self):
        with patch('hen_class.requests.get') as response:
            response.return_value.status_code = 200
            self.assertIsInstance(self.house.food_price(), int)

    def test_food_price_error(self):
        with patch('hen_class.requests.get') as response:
            response.return_value.status_code = 404
            self.assertRaises(ConnectionError, self.house.food_price())


if __name__ == '__main__':
    unittest.main()
