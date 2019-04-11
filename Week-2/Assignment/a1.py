def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
	if n % 50 == 0:
		return n // 50
	
	return n // 50 + 1
	
def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
	total__gains = 0.0
	total_losses = 0.0
	
	for value in price_changes:
		if value >= 0:
			total__gains += value
		else:
			total_losses += value
	
	return round(total__gains, 2), round(total_losses, 2)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

	starting = L[:k]
    lasts = L[-k:]
    L[-k:] = starting
    L[:k] = lasts

if __name__ == '__main__':
    import doctest
    doctest.testmod()
