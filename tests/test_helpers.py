from lib.random import ServiceObj
	
def test_set_instance_var_as_data(): 
	data = {"John" ,"Jack","Ben"}
	helper = ServiceObj()
	helper.set_input_data(data)

	assert helper.input_data == {"John" ,"Jack","Ben"}

def test_can_create_list():
	data = {"John" ,"Jack","Jill"}
	helper = ServiceObj()
	_list = helper.create_list(data)

	assert isinstance(_list, list)

def test_can_set_list_data():
	data = {"John" ,"Jack","Jill"}
	helper = ServiceObj()

	assert len(helper.list_data) == 0

	_list = helper.create_list(data)
	helper.set_list_data(_list)

	assert len(helper.list_data) == 3