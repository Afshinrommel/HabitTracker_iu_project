""" The purpose of this function is to graphically 
display the progress of the user's habits
""" 

import plotext as plt

# It imports library of plotext

def plot_habit(habit_names,habit_progresses):
    plt.simple_bar(habit_names,habit_progresses, width= 100)
    plt.show()