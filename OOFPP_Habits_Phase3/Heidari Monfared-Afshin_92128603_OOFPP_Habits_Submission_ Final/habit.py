"""
This document contains habit class. The Habit class contains  functions for
 update ,add, delete anod other functions of user habits.It imports following 
 libraries.for example, sqlite3,questionary,json,plotext. It also calls the
internal functions of the files inside the folder. These files are placed 
separately in the same folder so that it is easier to change or update them 
and the program code is not too crowded.
"""

import sqlite3
from os.path import join, dirname, abspath
import questionary
from datetime import timedelta
from datetime import datetime as dt
import os
import plotext as plt
import computation
import intermediate
import analyze_habit
import json

# Habit class, this class used for creation or manipulations of all habits of user
class Habit:
    """
    This class used to represent a habit.

    Attributes
    ----------
habit_name: string , name of habit

period: string, weekly or daily
practice_time: string, the total number of hours that a daily or weekly habit was practiced.
datetime_of_creation: string, time of define or create a special habit.
trace_number: integer, trace_number: An integer value that serves as a random number used for tracking a user between two classes.
status: It has 4 options,started, completed, broken or completed before the specific date.
datetime_of_completion:string , time of completion of a habit.
total_practice_time:string, the total number of hours allotted to the user to perform a daily or weekly habit. 
last_alter_date:string, the last time a habit was updated.
last_practice_time:string, string, this feature shows the number of hours a daily or weekly habit was practiced last time.
conn: establishing a connection to the database
    Methods
    -------
    get_specific_habit()
This method shows detailed information for a specific habit
    delete_habit_in_database()
This method deletes the history of practice time for a specific habit.
    save_habit_in_dataBase()
This method stores a new habit in the database.
    save_new_practice_time()
This method stores new practice time for a specific habit.
    see_last_alter_habits()
This method  displays the updated habits since a specific time.
    weekly_habit()
This method  displays all weekly habits.
    daily_habit()
This method displays all daily habits.
    all_habit()
This method displays habit progress both numerically and graphically.
    delete_habit()
This method deletes a specific habit from the database.
    longest_habit()
This method shows the longest streak of a daily or weekly habit. 
        edit_habit():
This method updates the following attributes for a specific habit.
habit_name, period, practice_time, status, date of creation,
time of completion,total_practice_time
Whenever the user performs a habit,she/he updates the parameter practice_time,
the value that are entered are not only added to the previous values,
but the activity time of that habit and its date are also recorded in the database.
    reset_history():
If the time or state of a previously defined habit undergoes a change to
the current day or the initial state, respectively, this function will
remove the previously recorded times from the database and modify the 
most recent state of the habit change to reflect the current day.
    """
# The __init__ function is called every time an object is created from Habit class
    def __init__(self,habitInfo):
        dp_Path_File = join(dirname(abspath(__file__)), 'databaseFile.db')
        self.connect = sqlite3.connect(dp_Path_File)
        self.curr = self.connect.cursor()
        dp_Path_Filex = join(dirname(abspath(__file__)), 'test.db')
        self.connectx = sqlite3.connect(dp_Path_Filex)
        self.currx = self.connectx.cursor()
        self.habit_name = habitInfo[0]
        self.period = habitInfo[1]
        self.practice_time = habitInfo[2]
        self.datetime_of_creation= habitInfo[3]
        self.trace_number = habitInfo[4]
        self.status = habitInfo[5]
        self.datetime_of_completion = habitInfo[6]
        self.total_practice_time = habitInfo[7]
        self.last_alter_date = habitInfo[8]
        self.last_practice_time = habitInfo[9]

# Show detail information of a habit and also It shows 
# the amount of progress numerically and graphically
    def get_specific_habit(self,habit_name):
         print("specific habit")              
         self.curr.execute(f"SELECT * FROM Habit WHERE habit_name = '{habit_name}' "
                      f"AND trace_number = '{self.trace_number}';")
         items = self.curr.fetchall()
         self.currx.execute(f"SELECT * FROM testtable")
         List = self.currx.fetchall()
         
         history_habit  = {}
         for row in List:
          s = json.loads(row[0])
          arrayx = [] 
          for x in s:
           arrayx.append(x)
          if arrayx[0] == habit_name and arrayx[1]==self.trace_number:
           history_habit.update({arrayx[3]:arrayx[2]})
#           history_habit.update({arrayx[0]:[arrayx[0],arrayx[2],arrayx[3]]})
           print(arrayx[2]+' hours added'+ ' on '+ arrayx[3])             
         try:
                print("habit number is",items[0][0] )
                print("period is",items[0][1] )
                print(f"practice_time is, {items[0][2]} hours until now")
                print("date of creation is",items[0][3] )
                print("datetime of completion is",items[0][6] )
                print(f"total_practice_time was defined {items[0][7]} hours from initial date" ) 
                print(f"last_alter_date is {items[0][8]}") 
                print(f"last_practice_time is {items[0][9]}") 
                progress = computation.comp(items[0][3],items[0][6],items[0][1],items[0][2],items[0][0],items[0][7],items[0][5])
                self.curr.execute(f"UPDATE Habit SET status = '{progress[2]}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                if progress[2] == 'Completed before specific day' and items[0][5] != 'Completed before specific day':
                    currentday = dt.now()
                    print("datetime of completion is updated",currentday)
                    self.curr.execute(f"UPDATE Habit SET datetime_of_completion = '{currentday}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")               
                self.connect.commit()
                print("status is",progress[2] )
                print("Your progress is ",progress[0],"and",progress[1], "hours remaining")
                os.system ('pause')  
                plt.clear_data()                
                diagtext = [items[0][0],'total progress']
                percent = [progress[0],1]
                plt.bar(diagtext,percent,orientation = "horizontal", width = 3 / 5)
                plt.show()
                os.system ('pause')
                plt.clear_data()
                os.system('cls')
                return_habit = [items[0][0]]
                return([return_habit,history_habit])
         except:
                print("habit name is not valid")
                return None
                os.system ('pause')
# as soon as a habit is deleted, this method delete practice history for a habit
    def delete_habit_in_database(self,habit_name,trace_number):
        self.currx.execute(f"SELECT * FROM testtable")
        List = self.currx.fetchall()
        self.currx.execute(f'DELETE FROM testtable;',)
        for row in List:
          s = json.loads(row[0])
          if s[0] == habit_name and s[1] == trace_number:
              pass
          else:
              jarray = json.dumps(s)
              self.currx.execute("INSERT INTO testtable (chaxarray) VALUES(' " + jarray + "')")
              self.connectx.commit()
        self.connectx.close()
    def save_habit_in_dataBase(self):
        self.curr.execute("INSERT INTO HABIT VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (self.habit_name, self.period, self.practice_time,self.datetime_of_creation,self.trace_number,self.status,self.datetime_of_completion,self.total_practice_time,self.last_alter_date,self.last_practice_time))      
        self.connect.commit()
        self.connect.close()
        self.save_new_practice_time(self.habit_name,self.trace_number,self.practice_time)
        print("new habit saved in Database")
        return(self.trace_number)
        os.system ('pause')
# store new habit into database
    def save_new_practice_time(self,habit_name,trace_number,new_excersise_time_hour):
        today = dt.now() 
#        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
        date_time = today.strftime("%m/%d/%Y")
        mix_array = []
        mix_array.append(habit_name)
        mix_array.append(trace_number)
        mix_array.append(new_excersise_time_hour)
        mix_array.append(date_time)
        jarray = json.dumps(mix_array)
        self.currx.execute("INSERT INTO testtable (chaxarray) VALUES(' " + jarray + "')")
        self.connectx.commit()
        self.connectx.close()
    
# this method specifies which habits have been updated since a given time         
    def see_last_alter_habits(self,period,alter_day):
#           period = questionary.rawselect("What's period?",
#            choices=["Daily", "Weekly"],).ask()
           if  period == "Daily":
#                print("How many days ago you alter habits ")
#                alter_day = intermediate.dig_input()
                today = dt.now()
                alter_duration = timedelta(days= int(alter_day)
                                           )
                alter_day = today - alter_duration
                day = alter_day.strftime("%Y-%m-%d %H:%M:%S")
                self.curr.execute(f"SELECT last_alter_date from Habit WHERE period = '{period}' "
                            f"AND trace_number = '{self.trace_number}';")
                items = self.curr.fetchall()
                get_list = []
                retrive_habit = []
                for item in items:
                 get_list.append(item[0])                
                for iter in get_list:
                     if iter > day:
                         self.curr.execute(f"SELECT habit_name from Habit WHERE last_alter_date = '{iter}' "
                            f"AND trace_number = '{self.trace_number}';")
                         retrive_habit_name = self.curr.fetchall()
                         retrive_habit.append(retrive_habit_name[0])
                         print(iter)
                         print(retrive_habit_name[0])
                         return(retrive_habit)

           if  period == "Weekly":
#                print("How many weeks ago you alter habits ")
#                alter_week = intermediate.dig_input()
                today = dt.now()
                alter_duration = timedelta(weeks= int(alter_day)
                                           )
                alter_week = today - alter_duration
                day = alter_week.strftime("%Y-%m-%d %H:%M:%S")
                self.curr.execute(f"SELECT last_alter_date from Habit WHERE period = '{period}' "
                            f"AND trace_number = '{self.trace_number}';")
                items = self.curr.fetchall()
                get_list = []
                retrive_habit = []
                for item in items:
                 get_list.append(item[0])
                for iter in get_list:
                     if iter > day:
                         self.curr.execute(f"SELECT habit_name from Habit WHERE last_alter_date = '{iter}' "
                            f"AND trace_number = '{self.trace_number}';")
                         retrive_habit_name = self.curr.fetchall()
                         retrive_habit.append(retrive_habit_name[0])
                         print(iter)
                         print(retrive_habit_name[0])
                         return(retrive_habit)  
                         
# this method shows list of all weekly habits    
    def weekly_habit(self):
        self.curr.execute(f"SELECT habit_name FROM Habit WHERE period = 'Weekly' AND trace_number = '{self.trace_number}'")
        items = self.curr.fetchall()
        habit_names = []
        for item in items:
            habit_names.append(item[0])
        print(habit_names) 
        return(habit_names)
# this method shows list of all daily habits
    def daily_habit(self):
        self.curr.execute(f"SELECT habit_name FROM Habit WHERE period = 'Daily' AND trace_number = '{self.trace_number}'")
        items = self.curr.fetchall()
        habit_names = []
        for item in items:
            habit_names.append(item[0])
        print(habit_names)
        return(habit_names)
# this method shows list of all habit, the amount of progress numerically and graphically
    def all_habit(self):
        print("These are your habit list")
        self.curr.execute(f"SELECT habit_name FROM Habit WHERE trace_number = '{self.trace_number}'")
        items = self.curr.fetchall()
        get_list = []
        habit_name_array= []
        habit_progress_array=[]
        list_of_all_habit_name = []
        number = 0
        for item in items:
            get_list.append(item[0])
        for i in get_list:
             self.curr.execute(f"SELECT * FROM Habit WHERE habit_name = '{i}' "
                      f"AND trace_number = '{self.trace_number}';")
             itemsx = self.curr.fetchall()
             get_listx = []    
             for i in itemsx:
              get_listx.append(i)
              
              os.system('cls')
              number = number + 1
              print("habit number is" , number)
              print("habit name is",get_listx[0][0])
              list_of_all_habit_name.append(get_listx[0][0])
              print("period is",get_listx[0][1] )
              print(f"practice_time is, {get_listx[0][2]} hours until now")
              print("date of creation is",get_listx[0][3] )
              print("date of completion is ",get_listx[0][6] )
              print(f"total_practice_time was defined {get_listx[0][7]} hours from initial date" )
              print(f"last_alter_date is {get_listx[0][8]}") 
              print(f"last_practice_time is {get_listx[0][9]}") 
              progress = computation.comp(get_listx[0][3],get_listx[0][6],get_listx[0][1],get_listx[0][2],get_listx[0][0],get_listx[0][7],get_listx[0][5])
              
              self.curr.execute(f"UPDATE Habit SET status = '{progress[2]}' WHERE habit_name = '{get_listx[0][0]}' "
                                    f"AND trace_number = '{self.trace_number}';")
              
              if progress[2] == 'Completed before specific day' and get_listx[0][5] != 'Completed before specific day':
                    currentday = dt.now()
                    print("datetime of completion is updated",currentday)
                    self.curr.execute(f"UPDATE Habit SET datetime_of_completion = '{currentday}' WHERE habit_name = '{get_listx[0][0]}' "
                                    f"AND trace_number = '{self.trace_number}';") 

              self.connect.commit()
              print("status is",progress[2] )
              print("Your progress is ",progress[0],"and",progress[1], "hours remaining")
              habit_name_array.append(get_listx[0][0])
              habit_progress_array.append(progress[0])    
              os.system ('pause')
              os.system('cls')
             os.system ('pause')
             os.system('cls')
        plt.clear_data()     
        analyze_habit.plot_habit(habit_name_array,habit_progress_array)
        return(list_of_all_habit_name)


# This function resets the time of creation and subsequently deletes the history of practice time for the corresponding habit.
    def reset_history(self,habit_name,trace_number):
        new_datetime_of_creation = dt.now()                 
        self.curr.execute(f"UPDATE Habit SET datetime_of_creation = '{new_datetime_of_creation}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
        self.curr.execute(f"UPDATE Habit SET practice_time = '{0}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{trace_number}';")  
        now = dt.now()
        self.curr.execute(f"UPDATE Habit SET last_alter_date = '{now}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{trace_number}';")  
        self.curr.execute(f"UPDATE Habit SET last_practice_time = '{0}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{trace_number}';")
        self.delete_habit_in_database(habit_name,trace_number) 
        print('The start time of the routine was changed to today, and the previous record of the routine was deleted.')  
        print('Please updaue date of completion if it is necessary!') 

# delete a habit from database        
    def delete_habit(self,habit_name):
       items = None
       self.curr.execute(f"SELECT * FROM Habit WHERE habit_name = '{habit_name}' "
        f"AND trace_number = '{self.trace_number}';")
       items = self.curr.fetchall()
       
       if len (items) != 0:
          self.delete_habit_in_database(habit_name,self.trace_number)       
          self.curr.execute(f"DELETE FROM Habit WHERE habit_name = '{habit_name}' AND trace_number = '{self.trace_number}';")
          self.curr.fetchall()
          self.connect.commit()
          print(f"'{habit_name}' successfully deleted.")
          
       else:
          print("Habit name is inavalid")
    
       return(habit_name)
# Among all daily or weekly habits, it shows the longest time           
    def longest_habit(self,period):
        self.curr.execute(f"SELECT habit_name FROM Habit WHERE trace_number = '{self.trace_number}'")
        items = self.curr.fetchall()
        get_list = []
        number = 0
        compare_list_number = []
        compare_list_name = []
        for item in items:
            get_list.append(item[0])
        for i in get_list:
             self.curr.execute(f"SELECT * FROM Habit WHERE habit_name = '{i}' "
                      f"AND trace_number = '{self.trace_number}';")
             itemsx = self.curr.fetchall()
             get_listx = []  
  
             for i in itemsx:
              get_listx.append(i)
              os.system('cls')
              number = number + 1
              diff = computation.comp_period(get_listx[0][3],get_listx[0][6])
              if get_listx[0][1] == period:
                compare_list_name.append(get_listx[0][0])
                compare_list_number.append(diff) 
        max_value = max(compare_list_number)
        index_max_value = compare_list_number.index(max_value)
        habit_max_value = compare_list_name[index_max_value]
        if period == 'Weekly':
            print ("the longest period time for habit name =" ,habit_max_value,"is",(max_value.days) / 7, 'weeks')
        if period == 'Daily':
            print ("the longest period time for habit name =" ,habit_max_value,"is",(max_value.days), 'days')
        return habit_max_value





#this method update following attributes for specific habit, habit_name,
#  period, practice_time, status, date of creation
# ,time of completion,total_practice_time  		
    def edit_habit(self):
                       
       questions = questionary.rawselect(
       "You can change habit_name, period, practice_time, status, date of creation,time of completion,total_practice_time?",choices=["habit name", "period","status", "date of creation", "total_practice_time","practice_time","time of completion"],).ask()
       
       if questions == "habit name":
        self.curr.execute(f"SELECT habit_name FROM Habit WHERE trace_number = '{self.trace_number}';")
        habit_names = self.curr.fetchall()
        habits = []
        i = -1
        for item in habit_names:
                i = i + 1
                habits.append(item[0])
                print("Your current habit name is", habits[i])
                question = questionary.rawselect(
       "Are you sure to change this habit name?",
                choices=["y", "n"],).ask()
                if question == "y":
                                    new_habit_name = intermediate.habit_name()
                                    self.curr.execute(f"UPDATE Habit SET habit_name = '{new_habit_name}' WHERE habit_name = '{habits[i]}' "
                                    f"AND trace_number = '{self.trace_number}';")
                                    self.connect.commit()
                else:
                    pass

       if questions == "period":
             try:     
              habit_name = intermediate.habit_name()   
              self.curr.execute(f"SELECT period from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
              period = self.curr.fetchall()
              period = period[0][0]
              print("Your current period is" , {period})
              new_period = questionary.rawselect("Daily,Weekly",
              choices=["Daily","Weekly"]).ask()
              self.curr.execute(f"UPDATE Habit SET period = '{new_period}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
              self.connect.commit()
             except:
              print("habit name is not valid")
              os.system ('pause')  

       if questions == "status":
            try:
                habit_name = intermediate.habit_name()
                self.curr.execute(f"SELECT status from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                status = self.curr.fetchall()
                status = status[0][0]
                print("Your current status is" , {status})
                new_status = questionary.rawselect("Completed,Started",
                choices=["Completed","Started"]).ask()

                self.curr.execute(f"UPDATE Habit SET status = '{new_status}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")                
                if new_status == 'Started':
                    self.reset_history(habit_name,self.trace_number)
                if new_status == 'Completed':
                    self.curr.execute(f"SELECT total_practice_time from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                    total_practice_time = self.curr.fetchall()
                    total_practice_time = total_practice_time[0][0]
                    self.curr.execute(f"UPDATE Habit SET practice_time = '{total_practice_time}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                self.connect.commit()
            except:
                 print("habit name is not valid")
                 os.system ('pause') 
       if questions == "date of creation":
             habit_name = intermediate.habit_name()
             
             try:    
                self.curr.execute(f"SELECT datetime_of_creation from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                datetime_of_creation = self.curr.fetchall()
                datetime_of_creation = datetime_of_creation[0][0]
                print("Your previous date of creation was" , {datetime_of_creation})
                new_status = 'Started'
                self.curr.execute(f"UPDATE Habit SET status = '{new_status}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")  
                self.reset_history(habit_name,self.trace_number)   
                self.connect.commit()
             except:
              print("habit name is not valid")
              os.system ('pause') 

       if questions == "practice_time":
           habit_name = intermediate.habit_name()
           try: 
              self.curr.execute(f"SELECT practice_time from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
              practice_time = self.curr.fetchall()
              practice_time = practice_time[0][0]
              print(f"Your practice time is , {practice_time} hours")
              print('new time will be added to previous value')
              new_excersise_time_hour = intermediate.dig_input()
              self.save_new_practice_time(habit_name,self.trace_number,new_excersise_time_hour)
#           
              practice_time = float(practice_time) + float(new_excersise_time_hour)
              
              self.curr.execute(f"UPDATE Habit SET practice_time = '{practice_time}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")  
              now = dt.now()
              self.curr.execute(f"UPDATE Habit SET last_alter_date = '{now}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';") 
              
              self.curr.execute(f"UPDATE Habit SET last_practice_time = '{new_excersise_time_hour}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';") 
              self.connect.commit()          
              
           except:
              print("habit name is not valid")
              os.system ('pause') 
                           
       if questions == "time of completion":
             habit_name = intermediate.habit_name()
             try: 
                self.curr.execute(f"SELECT datetime_of_completion from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                time_of_completion = self.curr.fetchall()
                time_of_completion = time_of_completion[0][0]
                print("Your current time of completion is" , {time_of_completion})
                print('Expected days for completion')
                expected_day = intermediate.dig_input()
#                expected_day = questionary.text("Expected days for completion").ask()
                event_duration = timedelta(days= int(expected_day))
                date_of_creation = dt.now()
                new_time_of_completion = date_of_creation + event_duration

                self.curr.execute(f"UPDATE Habit SET datetime_of_completion = '{new_time_of_completion}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                self.curr.execute(f"UPDATE Habit SET status = 'Started' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                
                self.connect.commit()                
             except:
              print("habit name is not valid")
              os.system ('pause') 

       if questions == "total_practice_time":
             habit_name = intermediate.habit_name()
             try: 
                self.curr.execute(f"SELECT total_practice_time from Habit WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
                total_practice_time = self.curr.fetchall()
                total_practice_time = total_practice_time[0][0]
                print(f"Your total practice time is {total_practice_time} hours")
                new_total_practice_time = intermediate.dig_input()
#                new_total_practice_time = questionary.text("Expected total practice time is").ask()
  
                self.curr.execute(f"UPDATE Habit SET total_practice_time = '{new_total_practice_time}' WHERE habit_name = '{habit_name}' "
                                    f"AND trace_number = '{self.trace_number}';")
            
                self.connect.commit()
             except:
              print("habit name is not valid")
              os.system ('pause') 

           







