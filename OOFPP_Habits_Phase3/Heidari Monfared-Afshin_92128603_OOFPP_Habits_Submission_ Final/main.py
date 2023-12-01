import questionary
import initialize
from InquirerPy import inquirer
import to_do
import habit
import edit_profile
import chk_user
import make_habit
import intermediate
import string
import logo

"""The program initiates by executing this file and subsequently 
enrolls a new user while establishing habits for the associated user.
The process of updating the user's information and habits can be
achieved by calling the functions and methods that have been
imported in this file.
Both the Habit and User classes are invoked in this file, resulting in the
creation of a new user through the execution of the method specified 
within the User class. Additionally, by invoking methods within the
Habit class, a new habit can be created.

By calling the functions lunch_db() and lunch_dbx() inside the file `initialize`,
 it enables connection with the database and creates the relevant tables.
Predefined habits are asked from the user, and finally, the user can create
 a new habit in addition to the previous habits.
""" 
conn = initialize.lunch_db()
connx = initialize.lunch_dbx()
initialize.create_table(conn)
initialize.create_tablex(connx)
welcome_message =  "this is the app for tracking habits"
print (welcome_message)
print(logo.logo)
progress = True
# It is possible to use the program until the user exits it.
while progress:
    question = questionary.rawselect(
    "register user or login or exit?",
    choices=["Register new user", "Login", "Exit"],
).ask()
    if question == 'Exit':
     progress = False
     print("Program exited")

    if question == 'Register new user':
             print('registering ....')  
             already_user = True
             while already_user == True:
                try:
                  th = initialize.user_registeraion()
                  already_user = chk_user.chkUser(th[0],th[1])
                  if already_user == False:
                     new_user = to_do.User(th)
                     new_trace_number = new_user.save_user_in_database()
                     initial_habit_array = ["Reading","Studying","Cycling","Running","Cleaning"]
                     for index in initial_habit_array:
                       make_habit.habit_making(index,new_trace_number)
                     question = questionary.rawselect(
       "Would you like to add new habit?",choices=["y", "n"],).ask()
                     if question == "y":
                       habit_name = inquirer.text(
                       message="habit_name:",
                       validate=lambda result: len(result) > 0 and result.isalpha(),
                       invalid_message="Input cannot be empty or number inside the strings.",
).execute()
                       habit_name = string.capwords(habit_name)  
                       make_habit.habit_making(habit_name,new_trace_number)
                except:
                  print("Something went wrong:Try again")
  
    if question == 'Login':
       print('loging ...')
       user = inquirer.text(
       message="Name:",
       validate=lambda result: len(result) > 0 and result.isalpha(),
       invalid_message="Input cannot be empty or number inside the strings.",
).execute()

       user = string.capwords(user)
       surname = inquirer.text(
       message="Surname:",
       validate=lambda result: len(result) > 0 and result.isalpha(),
       invalid_message="Input cannot be empty or number inside the strings.",
).execute()
       surname = string.capwords(surname)  
       
       password = inquirer.secret(
       message="Password:",
       validate=lambda result: len(result) > 0 and result.isalpha(),
       invalid_message="Input cannot be empty or number inside the strings.",
).execute()
       password = string.capwords(password)
       thislist = []
       thislist.append(user)
       thislist.append(surname) 
       thislist.append(password)
       userx = to_do.User(thislist)
       ch = userx.check_user()
       if ch[0] == False:
         print("Invalid username or password.\n")
       else:
         trc_number = ch[1]
         print("Valid username.\n")
         progressing = True
         while progressing:

            question = questionary.rawselect("Habit update, edit profile or exit?",
            choices=["Habit","Edit profile","Exit"]).ask()

            if question == 'Exit':
               progressing = False
            if question == 'Edit profile':
               print("edit profile ....")
               x = edit_profile.edit_Profile(trc_number)
            if question == 'Habit':  
               question_habit = questionary.rawselect("all habit,longest habit,weekly habits,daily habits,specific habit,update habit,delete habit,add habit,see last alter habits,exit?",
                           choices=["all habit","longest habit","weekly habits","daily habits","specific habit","update habit","delete habit","add habit","see last alter habits","exit"]).ask()
               if question_habit == 'Exit':
                progressing = False
               if question_habit == 'weekly habits':
                thislist = intermediate.make_array(trc_number)
                weekly_habit = habit.Habit(thislist)
                weekly_habit.weekly_habit()
               if question_habit == 'specific habit':
                thislist = intermediate.make_array(trc_number)
                get_specific_habit = habit.Habit(thislist)
                habit_name = intermediate.habit_name() 
                get_specific_habit.get_specific_habit(habit_name)

               if question_habit == 'daily habits':
                thislist = intermediate.make_array(trc_number)
                daily_habit = habit.Habit(thislist)
                daily_habit.daily_habit()

               if question_habit == 'all habit':
                thislist = intermediate.make_array(trc_number)
                all_habit = habit.Habit(thislist)
                all_habit.all_habit()

               if question_habit == 'longest habit':
                thislist = intermediate.make_array(trc_number)
                longest = habit.Habit(thislist)
                period = questionary.rawselect(
                "Daily or Weekly?",
                choices=["Daily", "Weekly"],
                ).ask()
                longest.longest_habit(period)

               if question_habit == 'add habit':
                  habit_name = intermediate.habit_name()
                  make_habit.habit_making(habit_name,trc_number)
               
               if question_habit == 'delete habit':
                habit_name = intermediate.habit_name()
                thislist = intermediate.make_array(trc_number)
                delete_habit = habit.Habit(thislist)
                delete_habit.delete_habit(habit_name)
               if question_habit == 'update habit':
                thislist = intermediate.make_array(trc_number)
                edit_habit = habit.Habit(thislist)
                edit_habit.edit_habit()

               if question_habit == 'see last alter habits':
                 period = questionary.rawselect("What's period?",
                 choices=["Daily", "Weekly"],).ask()
                 
                 print("How many days or weeks ago you did alter habits?")
                 alter_day = intermediate.dig_input()
                    
                 thislist = intermediate.make_array(trc_number)
                 see_last_alter_habits = habit.Habit(thislist)
                 see_last_alter_habits.see_last_alter_habits(period,alter_day)

                
          


    

 