# Author: Emma Slagle
# Date: 8/4/2024
# Project Title: ʻOlelo Hawaiʻi Timer

import tkinter as tk
import datetime
#Suppress Tk deprecation warning. 
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
is_countdown_active = False

#Convert time entry to int & start countdown
def start_timer():
    global is_countdown_active
    reset_timer() #reseting timer to ensure multiple countdowns don't commence at once
    try: 
      #converting entry in mins, to secs
      time_left = int(entry.get()) * 60 
      #start countdown
      is_countdown_active = True 
      countdown(time_left)
    except ValueError:
    #if user entered a non numerical entry
        timer_label.config(text="E ʻoluʻolu enter a valid helu", font=("Helvetica", 20))

#Countdown function
def countdown(time_left):
    global is_countdown_active
    if not is_countdown_active:
      return
    mins, secs = divmod(time_left, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}") 
    if time_left > 0:
      root.after(1000, countdown, time_left - 1)
    else: 
      timer_label.config(text="Pau!", fg="blue")
      
#Resetting timer display
def reset_timer(): 
   global is_countdown_active
   is_countdown_active = False
   timer_label.config(text="00:00")

#ITS WIDGET TIME
#Setting up the main window
root = tk.Tk()
root.title("Countdown Timer/ Helu Uaki eh")
root.config(bg="black") 

#Get and display current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
date_label = tk.Label(root, text=f"Lā o kēia lā: {current_date}", font=("Helvetica", 16), fg="gray", bg="black")
date_label.pack(pady=(10,0))

#Entry widget to input seconds
entry = tk.Entry(root, width=10) 
entry.pack(pady=20) 

#Timer label
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 50), fg="red", bg="black") 
timer_label.pack(pady=(5,10))

#Start and reset buttons
start_button = tk.Button(root, text="Hoʻomaka", font=("Helvetica", 15), fg="blue", command=start_timer)
start_button.pack(side="left", padx=(10,35), pady=7)    
reset_button = tk.Button(root, text="Hoʻopau", font=("Helvetica", 15), fg="red", command=reset_timer)
reset_button.pack(side="right", padx=(35,10), pady=7)

#Run
root.mainloop()
