from tkinter import *
import math
#constants
pink = "#e2979c"
red = "#e7305b"
green = "#9bdeac"
yellow = "#f7f5dd"
fontName = "Courier"
workMin = 0.2
shortBreakMin = 0.1
longBreakMin = 20
repetitions = 0
timer = None #none is basically our null

#timer reset
def resetTimer():
    root.after_cancel(timer) #after_cancel cancels the after function
    canvas.itemconfig(timerText, text="00:00")
    title.config(text="Timer")
    tick.config(text="")

#timer 

def startTimer():
    global repetitions
    repetitions += 1
    workSec = workMin * 60
    shortBreakSec = shortBreakMin * 60
    longBreakSec = longBreakMin * 60

    if repetitions % 8 == 0:
        countDown(longBreakSec)
        title.config(text="Break", fg=red)

    elif repetitions % 2 == 0:
        countDown(shortBreakSec)
        title.config(text="Break", fg=pink)
    else:
        countDown(workSec)
        title.config(text="Work")


#countdown stuff
def countDown(count): 

    countMin = math.floor(count / 60) 
    countSec = count % 60

    if countSec < 10:
        countSec = f"0{countSec}" 
    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = root.after(1000, countDown, count - 1)#calling countdown because need to update seconds every second
    else:
        startTimer()
        mark = " "
        workSessions = math.floor(repetitions/2)
        for i in range(workSessions):
            mark += "✓"
        tick.config(text=mark)



#ui stuff

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=yellow)



title = Label(text="Timer", font=(fontName, 32, "bold"), fg=green, bg=yellow)
title.grid(column=1,row=0)


canvas = Canvas(width=200, height=224, bg=yellow, highlightthickness=0) 
hehe_img = PhotoImage(file="C:\Users\\rujut\\vs code python\hehe.png")
canvas.create_image(100, 112, image=(hehe_img))
timerText = canvas.create_text(103, 138, text="00:00", fill="white", font=(fontName, 35, "bold"))
canvas.grid(column=1,row=1)



start_button = Button(text="Start", highlightthickness=0, command=startTimer) #when you click start start_timer is called
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=resetTimer) #when you click reset resetTimer is called
reset_button.grid(column=2,row=2)

tick = Label(font=(fontName, 12, "bold"), fg=green, bg=yellow)
tick.grid(column=1,row=3)


root.mainloop()