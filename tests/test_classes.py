from lib.testing_class import TestingClass
from lib.vehicle import VehicleClass

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