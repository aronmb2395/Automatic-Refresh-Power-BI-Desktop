import subprocess
import sched
import time
import datetime

# Call with python the pbix_file
def pbi_automatic_launcher():
    subprocess.call(["python", r'C:\Users\USER\Documents\PowerBI Automate Refresh\pbi_refresh_configuration.py'])   



# Schedule the time when you want the pbi_file to be launched
scheduled_time = datetime.datetime.combine(datetime.date.today(), datetime.time( 19, 35, 1)) # HOUR, MINUTES, SECONDS
scheduled_time_timestamp = time.mktime(scheduled_time.timetuple())




# Execute the loop. Yo can define the days of the week you want to launch the pbi refresh as well as the frequency of each launch.

while True:
    now_date_time = datetime.datetime.now().replace(microsecond=0)
    day_of_week = now_date_time.weekday()
    
    if day_of_week in (0,1,2,3,4,5): # Define the weekdays we want to launch the pbi_file
        if now_date_time.time() == scheduled_time.time():
            s = sched.scheduler(time.time, time.sleep)
            s.enterabs(scheduled_time_timestamp,  1, pbi_automatic_launcher)
            scheduled_time = scheduled_time + datetime.timedelta(minutes=3) # Define the interval time you want to launch again the pbi_file
            s.run()
        else:
            time.sleep(1) # Define the interval time for running the code. Every second it will check the hour and date of the local machine to run the code
    else:
        time.sleep(86400) # Define the interval stop when it is weekend so the code will not be running wasting resources






