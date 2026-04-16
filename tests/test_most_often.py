from lib.most_often import *

# Test to see if one item appears most often

def test_returns_most_frequent_item():
    most = MostOften([1, 2, 1])
    assert most.get_most_often() == 1

# Test for two items being the same and resulting in a tie

def test_returns_no_clear_winner_when_two_the_same():
    most = MostOften([1, 2])
    assert most.get_most_often() == "no clear winner"

# Add new item to the list to get winner 

def test_add_new_item_to_list():
    most = MostOften([1, 2])
    most.add_new(1)
    assert most.get_most_often() == 1

# Add new iten to the list to get tie

def test_add_new_iten_to_list_for_tie():
    most = MostOften([1, 2, 1])
    most.add_new(2)
    assert most.get_most_often() == "no clear winner"

# Test to see if multiple items will tie

def test_to_see_if_no_clear_winner_on_multiple_tie():
    most = MostOften([1, 2, 3])
    assert most.get_most_often() == "no clear winner"
