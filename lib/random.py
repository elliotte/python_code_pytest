class ServiceObj():

	input_data = ""
	list_data = ""

	def loop_(self, phonebook):
		ins = phonebook
		result = []
		for name, number in ins.items():
			result.append("Phone number of %s is %d" % (name, number))

		return result

	def is_info_present(self, ilist, info):
		if info not in ilist:
			return "Not in List"
		if info in ilist:
			return "Yes in List"

	def create_list(self, data):
		return list(data)

	def set_input_data(self, data):
		self.input_data = data

	def set_list_data(self, data):
		self.list_data = data

	# def set_obj_data(self, _data):
