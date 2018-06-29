import pytest
import lib.functions
from lib.functions import *

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

