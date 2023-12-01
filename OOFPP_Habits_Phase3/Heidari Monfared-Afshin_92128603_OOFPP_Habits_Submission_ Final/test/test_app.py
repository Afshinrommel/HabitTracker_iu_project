 
import unittest
from freezegun import freeze_time
from datetime import datetime as dt
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import habit
import to_do
import initialize

def connect_to_database():
    db_connect = initialize.lunch_db()
    return(db_connect)

def connect_to_second_databse():
    db_connect_second= initialize.lunch_dbx()
    return(db_connect_second)



class name_Check(unittest.TestCase):

    def test_connect_database(self):
        db_connect = connect_to_database()
        assert db_connect is not None

    def test_connect_to_second_databse(self):
        db_connect_second = connect_to_second_databse()
        assert db_connect_second is not None
    @freeze_time('2023-11-25') 
    def test_get_habit_history(self):
        today = dt.now() 
        date_time = today.strftime("%m/%d/%Y")
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        get_specific_habit = habit.Habit(thislist)
        existing_habit = get_specific_habit.get_specific_habit('Reading')[1]
        assert (existing_habit[date_time] == '8')
#        assert len (existing_habit) > 0

    def test_save_habit_in_dataBase(self):
         self.curr = connect_to_database().cursor()
         habit_list = []
         habit_list.append('Yoga')
         habit_list.append('Daily')
         habit_list.append(6)
         habit_list.append('2021-11-14 01:33:02.425978')
         habit_list.append(234573846)
         habit_list.append('Started')
         habit_list.append('2022-11-14 01:33:02.425978')
         habit_list.append(120)
         habit_list.append('2020-11-14 01:33:02.425978')
         habit_list.append(5)
         self.connect = connect_to_database()
         save_habit = habit.Habit(habit_list)
         respond = save_habit.save_habit_in_dataBase()
         assert respond is not None

    def test_delete_specific_habit(self):
        self.curr = connect_to_database().cursor()
        self.currx = connect_to_second_databse()
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        del_habit =  habit.Habit(thislist)
        self.connect = connect_to_database()
        self.connectx = connect_to_second_databse()
        respond = del_habit.delete_habit('Yoga')
        assert respond is not None

                  
    def test_login_database(self):
        self.curr = connect_to_database().cursor()
        self.firstname = 'Afshin'
        self.surname = 'Afshin'
        self.password = 'Afshin'
        user = to_do.User.check_user(self)
        assert user is not None



        
    def test_get_habit(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        get_specific_habit = habit.Habit(thislist)
        existing_habit = get_specific_habit.get_specific_habit('Reading')[0]
        assert len(existing_habit) == 1
    
    def test_see_last_alter_habits(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        see_last_alter_habits = habit.Habit(thislist)
        existing_habit = see_last_alter_habits.see_last_alter_habits('Daily','100')
        non_existing_habit = see_last_alter_habits.see_last_alter_habits('D','1')
        assert len(existing_habit) == 1
        assert non_existing_habit is None
    def test_weekly_habit(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        weekly_habit = habit.Habit(thislist)
        existing_habit = weekly_habit.weekly_habit()
        assert len(existing_habit) >= 0
    def test_daily_habit(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        daily_habit = habit.Habit(thislist)
        existing_habit = daily_habit.weekly_habit()
        assert len(existing_habit) >= 0
    def test_all_habit(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        all_habit = habit.Habit(thislist)
        list_habit = set(['Reading', 'Studying', 'Cycling', 'Running', 'Cleaning'])
        existing_habit = set(all_habit.all_habit())
        result = (list_habit).issubset(existing_habit)
        assert result == True
    def test_longest_habit(self):
        thislist = ['*','*','*','*',97726747,'*','*','*','*','*']
        longest_habit = habit.Habit(thislist)
        existing_habit = longest_habit.longest_habit('Weekly')
        assert existing_habit is not None
    def test_register_user_database(self):
         self.curr = connect_to_database().cursor()
         self.firstname = 'majidnpo'
         self.surname = 'ahmadiknlo'
         self.password = 'xmojtabiaee'
         self.connect = connect_to_database()
         random_number = to_do.User.save_user_in_database(self)
         assert random_number is not None




