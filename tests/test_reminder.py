from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Amy")
    reminder.remind_me_to("Charge your car")
    result = reminder.remind()
    assert result == "Charge your car, Amy!"