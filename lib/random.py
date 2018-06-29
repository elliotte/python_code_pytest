class ServiceObj():

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
