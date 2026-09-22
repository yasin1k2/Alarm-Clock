# imports and global valuables
import tkinter as tk
from datetime import datetime
window = tk.Tk()
title = window.title("Alarm Clock")
window.resizable(width=False,height=False)
window.geometry("480x560")
current_time = datetime.now().strftime("%H:%M:%S")
current_time_comp = datetime.now().strftime("%H:%M")
time_lable = tk.Label(window, text=f"{current_time}", font=("Malgun Gothic", 30))
time_lable.grid(row=0, column=5)
alarm_time = None

# UI with tkinter
## show time
def show_time():
    global current_time_comp
    global current_time
    current_time = datetime.now().strftime("%H:%M:%S")
    current_time_comp = datetime.now().strftime("%H:%M")
    time_lable.config(text = f"{current_time}")
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
    global alarm_time
    print(f"Alarm set for {hour_entry.get()}:{minute_entry.get()}")
    alarm_time = f"{hour_entry.get()}:{minute_entry.get()}"

## button for submiting the time
set_alarm_button = tk.Button(window, text = "Set Alarm", width=9,height=2, command= set_alarm)
set_alarm_button.grid(row = 5 , column = 5)


# compare alarm time with now time
def comapare(current_time , alarm_time):
    while True:
        if alarm_time <= current_time_comp:
            print("Alarm")


# make a alarm sound


# main
window.mainloop()
