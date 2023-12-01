# Project Title

HabitTracker

## Table of Contents

- [General Information](#general-information)

- [Installation](#installation)

- [Required Package](#required-package)

- [Required Package for test](#required-package-for-test)

- [Usage and Functionalities](#usage-and-functionalities)

- [How to use program](#how-to-use-program)

- [Registration](#registration)

- [Login](#login)

- Habit

  -  Habit functions

     *    [save habit in dataBase](#save-habit-in-database)
  
     *  [see_last_alter_habits](#see-last-alter-habits)

     *  [weekly_habit](#weekly_habit)

     *  [daily_habit](#daily_habit)

     *  [all_habit](#all_habit)

     *  [delete_habit](#delete_habit)

     *  [longest_habit](#longest_habit)

     *  [specific_habit](#specific_habit)

  *  Update habit includes following functions

     * [total practice time](#total-practice-time)

     *  [time of completion](#time-of-completion)

     *  [practice time](#practice-time)

     *  [date of creation](#date-of-creation)

     *  [status](#status)

     * [period](#period)

     *  [habit_name](#habit_name)

* [how to test the program](#how-to-test-the-program)

* [contributing](#contributing)

### General Information

```
    The habit tracking tool has the capacity to serve as an exceedingly beneficial device for individuals
who aspire to establish new routinesor monitor their current habits.This particular software program
empowers users to establish their habits and track their progress over time. Additionally, the software
allows for the creation of progress reports. The data gathered is stored in a SQLite database, and
the program provides a user-friendly command interface, as well as habit analysis.

```

### Installation

```
The latest version of Python can be obtained by downloading it, and it is recommended to select the
"ADD to path" option during the installation process. Subsequent to installing Python, it becomes
imperative to proceed with the installation of the required libraries.

```

### Required Package

```
    The required packages, namely questionary, InquirerPy, bcrypt, sqlite3, DateTime, and plotext,freezegun,
pytest can be installed using the pip command.

```

### Required package for test

```
    The installation of pytest is essential for successfully executing tests, which can be achieved by
running the following command
"pip install -U pytest".

```

### Usage and Functionalities

### How to use program

```
    Please download all project files and folders onto your computer and then modify the default path
to the location where the downloaded files are stored.As an illustration, on a Windows operating system,
execute following subsequent command in the command prompt:cd change "Python filepath/foldername/main.py"
Afterwards, execute Python using the following command:
python main.py

```

### Registration

```
    There is potential for constructing a user profile. One is presented with the opportunity to enter their
first name and last name, along with their desired username and password. If the chosen username is already
taken, the user will be prompted to select a different one. Once all the necessary information has been provided
accurately, the user's profile will be successfully created, granting them  access to the program.
Afterward, one has the option of either following a predetermined habits or completely bypassing it.
Subsequently, the opportunity to introduce a new habit arises.

```

### Login

```
    To gain access to the system, it is necessary to input one's name, surname, and password. Upon successfully
verifying the correctness of these credentials, the user will be granted the option to either modify their profile,
manage their habits, or exit the system. If the user chooses to edit their profile, they will be able to update
their name, surname, or password. Alternatively, by selecting the "Habit" option, users will be able to customize
their habits according to their preferences.

```

### Habit

```
    If the user is able to successfully authenticate into the system, then upon selecting the habit option,
he/she will have the ability to make a selection from the list of available items.

```

### save habit in dataBase

    Add a new habit to database

### see last alter habits

```
    After the user designates the category of a habitual activity that occurs on a daily or weekly basis,
subsequent to a predetermined time as specified by the user, the user is able to observe the revised
habitual activities.

```

### weekly_habit

    The user's defined weekly habits are displayed.

### daily_habit

    The user's defined daily habits are displayed.

### all_habit

```
    The display includes all habits, encompassing those that are carried out on a daily basis as well as
those that are done on a weekly basis. For each habit, it provides a visual representation of the level
of advancement achieved, the specific time it commences, and the corresponding time it concludes, all
presented in numerical form. Lastly, it showcases the cumulative progress of all habits through
the use of a horizontal chart.

```

### delete_habit

```
    This function takes the name of a specific habit and then deletes
the habit from the database.

```

### longest_habit

```
    After designating the duration of the habit, either on a daily or weekly basis, the habit with the greatest
amount of time will be exhibited.

```

### specific_habit

```
    This particular function presents comprehensive details regarding a habit, encompassing both quantitative
and graphical representations of progress. Additionally, it provides a historical record of practice
time and the specific moments of updates pertaining to each habit.

```

### Update habit including following items

### total practice time

```
    This particular function alters the overall duration of time allocated to the user for the purpose of
executing and fulfilling a habitual behavior.

```

### time of completion

```
    The function possesses the capability to modify the designated termination time of a given habit.

```

### practice time

```
    Every time the user engages in practicing a habit, the system captures the duration of the practice
in hours as provided by the user. Subsequently, this value is added to the total sum of previous practice durations.
Moreover, the system meticulously records the duration of practice and the corresponding date exclusively
for the specific habit within the database.

```

### date of creation

```
    This specific function adjusts the starting time of the habit to match
the current day.

```

### status

```
    This specific function has the ability to determine the user's status, whether it is in the started or completed states.

```

### period

    This function can change the period from daily to weekly or vice versa.

### habit_name

    This function can change the name of a habit.

### How to test the program

```
    To execute the test file,to execute the test, obtain all the files, including the folder labeled
as "test," and transfer them to your personal computer.Additionally, two files, namely 'database main_db.db'
and 'test.db',  must already exist.These files are the original versions downloaded from the repository.
It is necessary to modify the path to the test folder. Finally, the following command should be executed.

python -m pytest -v test_app.py

```

### Contributing

```
    This marks the commencement of my initial undertaking in Python. I extend to you an invitation to provide
your esteemed comments, suggestions, and contributions. Please do not hesitate to contribute pull requests or
generate issues for bug reports and feature requests.

```
