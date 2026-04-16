from lib.counter import *

def test_counter_starts_at_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counted_to_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."