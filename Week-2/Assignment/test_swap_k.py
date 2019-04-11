import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for  a1.swap_k. """
	# Add your test methods for a1.swap_k here.
	def test_swap_k_empty_list(self):
        """ Test swap_k with a input ofn empty list """
        test_list = []
        a1.swap_k(test_list, 0)
        expected_result = []
		
        self.assertEqual(test_list, expected_result)

    def test_swap_k_one_element_list(self):
        """ Test swap_k with a input of a list of one element """
        test_list = [ 1 ]
        a1.swap_k(test_list, 0)
        expected_result = [ 1 ]
		
        self.assertEqual(test_list, expected_result)

    def test_swap_k_two_element_list_and_k_zero(self):
        """ Test swap_k  with a input of a list of 2 elements and k=0 """
        test_list = [ 1, 2 ]
        a1.swap_k(test_list, 0)
        expected_result = [ 1, 2 ]
		
        self.assertEqual(test_list, expected_result)

    def test_swap_k_two_element_list_and_k_1(self):
        """ Test swap_k  with a input of a list of 2 elements and k=1 """
        test_list = [ 1, 2 ]
        a1.swap_k(test_list, 1)
        expected_result = [ 2, 1 ]
		
        self.assertEqual(test_list, expected_result)

	def test_swap_k_odd_length_list_and_k_1(self):
        """ Test swap_k  with a input of an odd length list and and k=1  """
        test_list = [ 1, 2, 3, 4, 5 ]
        a1.swap_k(test_list, 1)
        expected_result = [ 5, 2, 3, 4, 1 ]
		
        self.assertEqual(test_list, expected_result)

    def test_swap_k_even_length_list_and_k_1(self):
        """ Test swap_k  with a input of an even length list and k=1  """
        test_list = [ 1, 2, 3, 4 ]
        a1.swap_k(test_list, 1)
        expected_result = [ 4, 2, 3, 1 ]
		
        self.assertEqual(test_list, expected_result)

    def test_swap_k_odd_length_list_and_k_0(self):
        """ Test swap_k  with a input of an odd length list and k=0 """
        test_list = [ 1, 2, 3, 4, 5 ]
        a1.swap_k(test_list, 0)
        test_list = [ 1, 2, 3, 4, 5 ]
		
        self.assertEqual(test_list, expected_result)
		
	def test_swap_k_even_length_list_and_k_0(self):
        """ Test swap_k  with a input of even length list and k=0 """
        test_list = [ 1, 2, 3, 4 ]
        a1.swap_k(test_list, 0)
        expected_result = [ 1, 2, 3, 4 ]
		
        self.assertEqual(test_list, expected_result)
		
		
if __name__ == '__main__':
    unittest.main(exit=False)
