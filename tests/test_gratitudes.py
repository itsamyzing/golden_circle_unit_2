from lib.gratitudes import *

def test_gratitude_is_empty():
    grats = Gratitudes()
    assert grats.format() == "Be grateful for: "

def test_gratitude_with_one_item():
    grats = Gratitudes()
    grats.add("family")
    assert grats.format() == "Be grateful for: family"

def test_gratitude_with_multiple():
    grats = Gratitudes()
    grats.add("home")
    grats.add("health")
    grats.add("work")
    assert grats.format() == "Be grateful for: home, health, work"