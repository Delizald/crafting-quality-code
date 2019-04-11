import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
	
	def test_num_buses_0_people(self):
		"""Test number of buses function with an input of 0 persons"""
		
		returned_result = a1.num_buses(0)
		expected_result = 0
		
		self.assertEqual(returned_result,expected_result)
		
	def test_num_buses_50_people(self):
		"""Test number of buses function with an input of 50 persons"""
		returned_result = a1.num_buses(50)
		expected_result = 1
		
		self.assertEqual(returned_result,expected_result)
		
	
	def test_num_buses_less_than_50_people(self):
		"""Test number of buses function with an input of less than 50 persons"""
		returned_result = a1.num_buses(25)
		expected_result = 1
		
		self.assertEqual(returned_result,expected_result)
		
	def test_num_buses_more_than_50_people(self):
		"""Test number of buses function with an input of more than 50 persons"""
		returned_result = a1.num_buses(75)
		expected_result = 1
		
		self.assertEqual(returned_result,expected_result)
	
if __name__ == '__main__':
    unittest.main(exit=False)
