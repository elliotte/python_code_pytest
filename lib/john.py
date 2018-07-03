class JohnMackay():
	is_organised = False
	left_house_yesterday = False
	todo_items_pending = 101
	is_a_wanker = True
	very_busy = False
	wallet = []
	memory = ""
	memory_sets = []

	def __init__(self):
		if self.todo_items_pending > 100:
			self.very_busy = True

	def leave_house(self):
		self.left_house_yesterday = True

	def is_at_max_lazy(self):
		if self.is_organised == False and self.very_busy == True and len(self.wallet) == 0:
			return True
		else:
			return False

	def load_memory(self, memories):
		self.memory = memories

	def isolate_day_memories(self):
		return list(self.memory.values())

	def note_memory_list(self, data):
		self.memory_sets = data

	def create_set(self, data):
		return set(data)