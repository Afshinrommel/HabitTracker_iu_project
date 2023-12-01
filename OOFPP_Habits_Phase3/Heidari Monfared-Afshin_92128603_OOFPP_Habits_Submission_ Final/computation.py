from datetime import datetime

# This function receives some information of a habit
#  and by comparing the start_date, final_date,practic_time,total_practice_time return
#  status of a habit (Completed on time, Completed before specific day, started and Broken) 
#  In addition to the above value, it returns the progress of a habit,status and the number 
#  of remaining hours to complete a habit
def comp(start_date,final_date,period,practic_time,habit_name,total_practice_time,status):
 
        staus_situation = status
        practic_time = float(practic_time)
        total_practice_time = float(total_practice_time)
        remain_hours = total_practice_time - practic_time
        
        
        if practic_time >= total_practice_time:
                practic_time = total_practice_time
                remain_hours = 0
        
        day1 = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
        day2 = datetime.strptime(final_date, '%Y-%m-%d %H:%M:%S.%f')
        currentday = datetime.now()
        
        progress = practic_time/total_practice_time

        if currentday > day2 and progress < 1:
               print("This habit is broken")
#               progress = 0
               staus_situation = 'Broken'
               return(progress, remain_hours, staus_situation)
        if currentday < day2 and progress == 1 or status =='Completed before specific day':
               print(f"This habit is established streak of '{currentday-day1}' periods")
               progress = 1
               staus_situation = 'Completed before specific day'
               return(progress, remain_hours, staus_situation)
        if currentday >= day2 and progress == 1 and status != 'Completed before specific day':
                print(f"This habit is completed on time")
                progress = 1
                staus_situation = 'Completed on time'
                return(progress, remain_hours, staus_situation)

        return(progress , remain_hours, staus_situation)
# This function takes two input valuesو start_date and final_date 
# of a habit and returns the difference between them
def comp_period(start_date,final_date):
        day1 = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
        day2 = datetime.strptime(final_date, '%Y-%m-%d %H:%M:%S.%f')
        diff = day2 - day1
        return(diff)
     
  

     
        


