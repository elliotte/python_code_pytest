from lib.john import *

def test_default_attributes():
	mong = JohnMackay()

	assert mong.is_organised == False
	assert mong.left_house_yesterday == False
	assert mong.todo_items_pending == 101
	assert mong.is_a_wanker == True
	assert mong.wallet == []

def test_john_can_leave_house():
	mong = JohnMackay()
	mong.leave_house()

	assert mong.left_house_yesterday == True	

def test_very_busy_auto_sets():
	mong = JohnMackay()

	assert mong.very_busy == True

def test_default_john_is_at_max_lazy():
	mong = JohnMackay()
	result = mong.is_at_max_lazy()

	assert result == True

def test_john_could_be_lazier():
	mong = JohnMackay()
	mong.wallet.append("Some Money")
	result = mong.is_at_max_lazy()	

	assert result == False

def test_john_can_remember_events():
	mong = JohnMackay()
	mong.load_memory({ "yesterday": ["Event 1", "Event 2", "Event 3"], "today": ["Event 1", "Event 2", "Event 3", "Event 0"]})

	assert len(mong.memory) == 2

def test_john_can_isolate_memories():
	mong = JohnMackay()
	mong.load_memory({ "yesterday": ["Event 1", "Event 2", "Event 3"], "today": ["Event 1", "Event 2", "Event 3", "Event 0"]})

	assert mong.isolate_day_memories() == [['Event 1', 'Event 2', 'Event 3'], ['Event 1', 'Event 2', 'Event 3', 'Event 0']]

def test_john_can_set_memory_list():
	mong = JohnMackay()
	mong.load_memory({ "yesterday": ["Event 1", "Event 2", "Event 3"], "today": ["Event 1", "Event 2", "Event 3", "Event 0"]})
	mong.note_memory_list(mong.isolate_day_memories())

	assert mong.memory_sets == [['Event 1', 'Event 2', 'Event 3'],['Event 1', 'Event 2', 'Event 3', 'Event 0']]

def	test_john_can_create_a_set():
	mong = JohnMackay()
	result = mong.create_set(["Event 1", "Event 2", "Event 3"])

	assert isinstance(result, set)

def test_john_can_find_memory_differences():
	mong = JohnMackay()
	mong.load_memory({ "yesterday": ["Event 1", "Event 2", "Event 3"], "today": ["Event 1", "Event 2", "Event 3", "Event 0"]})
	mong.note_memory_list(mong.isolate_day_memories())
	a_memory = mong.create_set(mong.memory_sets.pop())
	b_memory = mong.create_set(mong.memory_sets.pop())

	result = a_memory.difference(b_memory)

	assert result == {'Event 0'}



