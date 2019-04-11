import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
	def test_stock_price_summary_empty_list(self):
		"testing stock_price_summary function with an empty list as input"
		price_changes = []
		actual_result = a1.stock_price_summary(price_changes)
		expected_result = (0.0,0.0)
		
		self.assertEqual(actual_result, expected_result)
		
	def test_stock_price_summary_positive_value(self):
		"testing stock_price_summary function with a single positive value as input"
		price_changes = [5.0]
		actual_result = a1.stock_price_summary(price_changes)
		expected_result = (5.0,0.0)
		
		self.assertEqual(actual_result, expected_result)
		
	def test_stock_price_summary_negative_value(self):
		"testing stock_price_summary function with a single negative value as input"
		price_changes = [-5.0]
		actual_result = a1.stock_price_summary(price_changes)
		expected_result = (0.0,-5.0)
		
		self.assertEqual(actual_result, expected_result)
		
		
	def test_stock_price_summary_multiple_positive_negative_values(self):
		"testing stock_price_summary function with different negative and positive values as input"
		price_changes = [5.0,-5.0,3.0,-3.0,1,-1]
		actual_result = a1.stock_price_summary(price_changes)
		expected_result = (9.0,-9.0)
		
		self.assertEqual(actual_result, expected_result)
		
if __name__ == '__main__':
    unittest.main(exit=False)
