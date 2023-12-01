import questionary
import habit
import chk_habit
from datetime import datetime
from datetime import timedelta
import intermediate

# It imports the libraries questionary
#  datetime and documents of Intermediate and Habit, as well as chk_habit.
"""
habit_making(): This function prompts the user to enter the name of the habit.
If this habit has not been previously defined, the system will request 
the user to provide any additional necessary information.
Ultimately, the function generates an array and then return it.
"""


def habit_making(habit_name,trace_number):
    habit_exist = chk_habit.chk_habit(habit_name,trace_number)
    if habit_exist != True:
        habit_list = []
        print("Do you follow current habit?")
        question = questionary.rawselect(
        habit_name,
        choices=["Yes", "No"],
        ).ask()
        if question == 'Yes':
            date_of_creation = datetime.now() 
            print("How monay hours do you want to complete this habit?")
            total_practice_time = intermediate.dig_input()
            period = questionary.rawselect("What's period?",
            choices=["Daily", "Weekly"],).ask()
            if  period == "Daily":
                print("Expected days for completion")
                expected_day = intermediate.dig_input()
                while float(expected_day) * 24 <  float(total_practice_time):
                   print('Input is not valid')
                   expected_day = intermediate.dig_input()
                print("How monay hours did you practice today?")
                time_practic = intermediate.dig_input()
                while float(time_practic) > 24 or float(time_practic) < 0:
                   print('Input is not valid')
                   time_practic = intermediate.dig_input()
                event_duration = timedelta(days= int(expected_day))
                
            else :
                print("Expected weeks for completion")
                expected_week = intermediate.dig_input()
                while float(expected_week) * 24 * 7 <  float(total_practice_time):
                   print('Input is not valid')
                   expected_week = intermediate.dig_input()
                print("How many hours did you practice this week?")
                time_practic = intermediate.dig_input()
                while float(time_practic) > 168 or float(time_practic) < 0:
                 print('Input is not valid')
                 time_practic = intermediate.dig_input()
                event_duration = timedelta(weeks= int(expected_week))    
           
            last_practice_time = time_practic
            last_alter_date = date_of_creation
            datetime_of_completion = date_of_creation + event_duration

            habit_list.append(habit_name) 
            habit_list.append(period)
            habit_list.append(time_practic)
            habit_list.append(date_of_creation)
            habit_list.append(trace_number)
            habit_list.append("Started")
            habit_list.append(datetime_of_completion)
            habit_list.append(total_practice_time)
            habit_list.append(last_alter_date)
            habit_list.append(last_practice_time)
            new_habit = habit.Habit(habit_list)
            new_habit.save_habit_in_dataBase()
    