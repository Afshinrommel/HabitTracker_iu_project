import initialize

# It imports document of Initialize
"""
This function recives habit name and trace number. Subsequently, in the initial stage,
the system searches the provided information in the database. In the event that 
the those information are present, it return 'True' and subsequently program ask
new habit name from user.
"""

def chk_habit(habit_name,trace_number):
    conn = initialize.lunch_db()
    curr = conn.cursor()
    curr.execute(f"SELECT * FROM Habit WHERE habit_name = '{habit_name}' "
                      f"AND trace_number = '{trace_number}';")
    items = curr.fetchall()
    habits = []
    for item in items:
        habits.append(item[0])
    if len(habits)!= 0:
        print("!!This habit already exists in db, So you must choose another habit!!")
        return True
    else:
        return False



