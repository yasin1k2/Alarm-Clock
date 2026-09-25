# imports and global valuables
import tkinter as tk
from datetime import datetime
import pygame
window = tk.Tk()
title = window.title("Alarm Clock")
window.resizable(width=False,height=False)
window.geometry("480x560")
current_time = datetime.now().strftime("%H:%M:%S")
current_time_comp = datetime.now().strftime("%H:%M")
time_lable = tk.Label(window, text=f"{current_time}", font=("Malgun Gothic", 30))
time_lable.grid(row=0, column=5)
alarm_time = None
alarm_ringing = False
alarm_stopped = False


# UI with tkinter
## show time and compair
def show_time():
    global alarm_time
    global alarm_ringing

    current_time = datetime.now().strftime("%H:%M:%S")
    current_time_comp = datetime.now().strftime("%H:%M")
    time_lable.config(text = f"{current_time}")
    if alarm_time is not None and current_time_comp >= alarm_time and alarm_stopped == False :
        print("Alarm")
        alarm_ringing = True

    window.after(1000, show_time)
window.after(1000,show_time)

## boxes for inserting the alarm time
tk.Label(window, text = "Hour:").grid(row = 3 , column = 4)
hour_entry= tk.Entry(window, width=20)
hour_entry.grid(row= 3 , column = 5)
tk.Label(window, text = "Minute:").grid(row = 4, column = 4)
minute_entry= tk.Entry(window,width=20)
minute_entry.grid(row= 4 , column = 5)


## set alarm time
def set_alarm():
    global alarm_stopped
    global alarm_time

    alarm_stopped = False
    print(f"Alarm set for {hour_entry.get()}:{minute_entry.get()}")
    alarm_time = f"{hour_entry.get()}:{minute_entry.get()}"


## stop alarm
def stop_alarm():
    global alarm_ringing
    global alarm_stopped

    if alarm_ringing == True:
        alarm_stopped = True
        alarm_ringing =False



## button for submiting the time and stopping the alarm
set_alarm_button = tk.Button(window, text = "Set Alarm", width=9,height=2, command= set_alarm)
set_alarm_button.grid(row = 5 , column = 5)
stop_alarm_button = tk.Button(window, text = "Stop Alarm",width=9,height=2, command=stop_alarm )
stop_alarm_button.grid(row = 6 , column = 5)



# make a alarm sound


# main
window.mainloop()
