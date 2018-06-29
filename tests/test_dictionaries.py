from lib.random import ServiceObj

# simmilar to array but has key value relationship

def test_dictionary_loops():
	phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
	helper = ServiceObj()
	result = helper.loop_(phonebook)
	assert result == ['Phone number of John is 938477566', 'Phone number of Jack is 938377264', 'Phone number of Jill is 947662781']

def test_not_in_loop():
	phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
	helper = ServiceObj()
	
	result = helper.is_info_present(phonebook, "Nerd")
	assert result == "Not in List"
	
	result = helper.is_info_present(phonebook, "Jill")
	assert	result == "Yes in List"

	del phonebook['Jill']
	result = helper.is_info_present(phonebook, "Jill")
	assert result == "Not in List"