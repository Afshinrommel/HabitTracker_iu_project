import bcrypt
import sqlite3
from os.path import join, dirname, abspath
import random
import chk_trace

 
"""
This document describes our User class. Given that our software 
application has the capability to generate and manage multiple users,
all operations consistently refer to the user who is currently logged in. 
This section of code includes operations for generating and logging in a user profile.
"""
#It imports the libraries questionary, sqlite3,random,os.path,bcrypt.


# define this class for user representation.    
# THE USER CLASS.
"""Attributes
    ----------
    firstname: str
        the first name of the user
    surname: str
        the surname of the user
    trace_nubmer: Int
        random number
    password: str
        the password used by the user

    connect:
        Establishing a connection to the database

    Methods
    -------
    check_user()
       This method checks whether there is already a user with the same name and surname
       and also The process of accessing the database is accomplished by 
       providing the user's name, last name, and password using this method.
    save_user_in_dataBase()
    The process of registering a new user is carried out through this procedure,
    and the outcome of this mechanism is a numerical value that is used to 
    determine the current user's habit.
    save_user_in_dataBase()
    This function is responsible for storing the input data provided by the new user
    in the database. The data includes the name, surname, password, and a randomly 
    generated number. Prior to saving this number, the program ensures its uniqueness
    by invoking the 'chkTraceNumber' function within the 'chk_trace' document.
"""
class User:
    """
    Parameters
        ----------
        :param firstname: the firstname of the user
        :param surname: the surname of the user
        :param password: the password used by the user
    """
    def __init__(self,userInfo):
        dp_Path_File = join(dirname(abspath(__file__)), 'databaseFile.db')
        self.connect = sqlite3.connect(dp_Path_File)
        self.curr = self.connect.cursor()
        self.firstname = userInfo[0]
        self.surname = userInfo[1]
        self.password = userInfo[2]

# Logging the user and also preventing duplicate usernames
# and surnames for registration.
    def check_user(self):
        user_exists = False
        retrive_password = None
        c1 = self.curr.execute(f"SELECT * FROM User WHERE name = '{self.firstname}' "
                      f"AND surname = '{self.surname}';")
        result = c1.fetchone()
        if result:
              retrive_password = self.curr.execute(f"SELECT * FROM User WHERE name = '{self.firstname}'").fetchone()[2]
        else:
            pass
        if retrive_password != None: 
           if bcrypt.checkpw(self.password.encode('utf-8'), retrive_password):
               print("\n Login successful!\n")
               user_exists = True
               trc_number =  self.curr.execute(f"SELECT * FROM User WHERE name = '{self.firstname}'").fetchone()[3]
               return user_exists,trc_number
           else:
               print("\npassword is not true\n")
               user_exists = False
               return user_exists,0
        else:
           user_exists = False
        return user_exists,0
# This method stores a new user in the database.
    def save_user_in_database(self):
        trace_nubmer_exist = True
        while trace_nubmer_exist == True:
         random_number = random.randint(1,1000000000)
         trace_nubmer_exist = chk_trace.chk_trace_number(random_number)
         if trace_nubmer_exist != True:

          self.curr.execute("INSERT INTO USER VALUES(?, ?, ?, ?)",
                         (self.firstname, self.surname, self.password,random_number))
          self.connect.commit()
          self.connect.close()
          return(random_number)
         
