from lib.most_often import *

def test_retruns_most_frequent_item():
    most = MostOften([1, 2, 1])
    assert most.get_most_often() == 1

def test_returns_no_clear_winner_when_two_items_tie():
    most = MostOften([1, 2])
    assert most.get_most_often() == "no clear winner"

def test_returns_no_clear_winner_when_multiple_otems_tie():
    most = MostOften([1, 2, 1, 2])
    assert most.get_most_often() == "no clear winner"

def test_add_new_creates_a_winner():
    most = MostOften([1, 2])
    most.add_new(1)
    assert most.get_most_often() == 1

def test_add_new_creates_a_tie():
    most = MostOften([1, 1, 2])
    most.add_new(2)
    assert most.get_most_often() == "no clear winner"

def test_equal_count_branch_is_hit():
    most = MostOften([1, 1, 2, 2, 3])
    assert most.get_most_often() == "no clear winner"