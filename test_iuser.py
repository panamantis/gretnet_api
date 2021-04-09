import unittest
import sys,os
import re

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"
sys.path.insert(0,LOCAL_PATH)

from a_customer import Customer_Management

#0v1# JC Mar 17, 2021


class TestCustomer_Management(unittest.TestCase):
    def setUp(self):
        self.Customer_Manager=Customer_Management()

    def test_random_customer(self):
        customer_id=self.Customer_Manager.get_random_customer_id()
        self.assertGreater(len(customer_id),0)
        return

if __name__ == "__main__":
    unittest.main()


