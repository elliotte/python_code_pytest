# from mock import Mock
# from lib.decorators import cache

# def test_cache():

# 	my_fn = Mock(name='my_fn')
# 	my_fn.return_value = 'hi'

# 	wrapped = cache(my_fn)
# 	# First call gives a call count of 1
# 	assert wrapped(3) == 'hi'
# 	assert my_fn.call_count	== 1

# 	# Second call keeps the call count at 1 - the cached value is used
# 	# self.assertEqual(wrapped(3), 'hi')
# 	# self.assertEqual(my_fn.call_count, 1)

# 	# Subsequent call with a new value increased the call count
# 	# self.assertEqual(wrapped(7), 'hi')
# 	# self.assertEqual(my_fn.call_count, 2)