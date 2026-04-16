import pytest
from lib.present import *

#When we wrap an item we get it back when unwrapping

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

# No content has been wrapped

def test_that_no_present_has_been_wrapped():
    present = Present()
    present.wrap(0)
    assert present.unwrap() == 0

# Check a present has already been wrapped

def test_a_present_has_already_been_wrapped():
    present = Present()
    present.wrap(50)
    with pytest.raises(Exception) as e:
        present.wrap(55)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

# Check error message shows when no contents have been wrapped

def test_no_present_has_been_wrapped_shows_error_message():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message  = str(e.value)
    assert message == "No contents have been wrapped."


