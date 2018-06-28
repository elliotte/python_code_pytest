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
	# Passing but not working??
	assert lambda : my_function_with_args("Nerd", "DoOne") == "Hello, Nerd , From My Function!, I wish you DoOne"

############ 
#Standalone Tests
############

def test_challenge1():
    given = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert base64.b64encode(bytes.fromhex(given)) == expected

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
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

############ 
#Classes for tests
############

class TestingClass():
	variable = "Nerd"

	def class_function(self):
		return "Function called"

