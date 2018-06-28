import base64
import pytest

############ 
#Tests for Class
############

def test_testingClass_variable():
	obj = TestingClass()
	assert obj.variable == "Nerd"

def test_testingClass_func():
	obj = TestingClass()
	output = obj.class_function()
	assert output == "Function called"

def test_vehicle_func():
	car = VehicleClass()
	car.name = "Jump"
	car.color = "blue"
	car.kind = "van"
	car.value = 10000.00
	output = car.description()
	assert output == "Jump is a blue van worth 10000.00"

############ 
#Tests for Functions
############

def test_aFunction():
    with pytest.raises(SystemExit):
        small_function()

def test_in_operator():
	name = "John"
	list_of_names = ["Rick", "John"]
	assert name in list_of_names

def test_if_code_int():
	obj = 1
	result = if_statement_code(obj)
	assert result == "Int 1 Sent"

def test_if_code_string():
	obj = "WoW"
	result = if_statement_code(obj)
	assert result == "String Sent"

def test_if_code_other():
	obj = 3
	result = if_statement_code(obj)
	assert result == "Yes Sir"

def test_my_func_with_args():
	assert my_function_with_args("Nerd", "DoOne") == "Hello, Nerd , From My Function!, I wish you DoOne"

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

############ 
#Functions for tests
############

def small_function():
    raise SystemExit(1)

def if_statement_code(object):
	if object == 1:
		return "Int 1 Sent"
	elif object == "WoW":
		return "String Sent"
	else:
		return "Yes Sir"

def my_function_with_args(username, greeting):
    return "Hello, %s , From My Function!, I wish you %s"%(username, greeting)

############ 
#Classes for tests
############

class TestingClass():
	variable = "Nerd"

	def class_function(self):
		return "Function called"

class VehicleClass():
	name = ""
	kind = "car"
	color = ""
	value = 0.00
	def description(self):
		desc_str = "%s is a %s %s worth %.2f" % (self.name, self.color, self.kind, self.value)
		return desc_str

