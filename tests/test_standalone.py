import base64
import pytest

############ 
#Standalone Tests
############

def test_challenge():
    given = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert base64.b64encode(bytes.fromhex(given)) == expected

def test_dictionaries():
	ruby_hash_equivalent = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
	assert ruby_hash_equivalent == {'guido': 4127, 'jack': 4098, 'sape': 4139}
	#check index works the same as ruby
	assert ruby_hash_equivalent['guido'] == 4127

	assert list(ruby_hash_equivalent.keys()) == ['sape', 'guido', 'jack']
		# gotcha withour list is returns iterable views instead of lists

#not in ruby - an unordered collection with no dupicates
def test_sets():
	basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
	assert set(basket) == {'orange', 'banana', 'pear', 'apple'}