import unittest
from unittest import mock
import test_simple_employee
import utils

Employer = test_simple_employee.Employee('Ernest', 'M', 2000)


class EmployeeTestCase(unittest.TestCase):

    def test_email(self):
        self.assertEqual(Employer.email, 'ekedesh@gmail.com')

    def test_full_name(self):
        self.assertEqual(Employer.fullname, 'Ernest M')

    def test_employee_info(self):
        self.assertEqual(Employer.first, 'Ernest')
        self.assertEqual(Employer.last, 'M')
        self.assertEqual(Employer.pay, 2000)

    @mock.patch("utils.make_request", return_value=True)
    def test_monthly_schedule(self, month):
        response = utils.parse_response(Employer.last, 3)
        self.assertEqual(response, "Successful request")

    def test_raise(self):
        Employer.apply_raise()
        self.assertEqual(Employer.pay, 2100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
