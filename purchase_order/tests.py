from django.test import TestCase
from utils.utils import calculate_average

# Create your tests here.

class Test_PurchaseOrder(TestCase):

    def test_calculate_average(self):
        response = calculate_average(2,3)
        self.assertEqual(66.67,response) 

    def test_calculate_average_with_zero_division(self):
        response = calculate_average(0,3)
        self.assertEqual('00.00',response)

    def test_calculate_average_with_dividing_by_zero(self):
        response = calculate_average(3,0)
        self.assertEqual("100.00",response)

        

