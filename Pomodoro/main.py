from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#no of iteration is reps
reps=0
timer=""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    #stops the timer (pauses it)
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check.config(text="")

    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN *60
    long_sec = LONG_BREAK_MIN *60


    # if rep8 then long break of 20 min
    if reps %8==0:
        count_down(long_sec)
        label.config(text="Break",fg=RED)
    # if in rep2/4/6 then short break of 5 mins
    elif reps%2==0:
        count_down(short_sec)
        label.config(text="Break", fg=PINK)
    # if in rep1/3/5/7 then 25 min work
    else:
        count_down(work_sec)
        label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    #to display the starting minute as 5:00
    #dynamic typing
    if count_sec<10:
        count_sec=f"0{count_sec}"

    #special operation for canvas only,rest widgets cam be done using .config()method
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count>0:
        global timer
        #window does the process after specified milliseconds
        timer = window.after(1000,count_down,count-1)
    else :
        start_timer()
        marks= " "
        #floor method returns a whole number
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
#to increase the screen size
window.config(padx=100,pady=50,bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
#highlightthickness attribute removes the border around the image
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


#label
label=Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
label.grid(row=0,column=1)
check = Label(font=(FONT_NAME,24,"bold"),fg=GREEN,bg=YELLOW)
check.grid(row=3,column=1)

#buttons
start = Button(text="Start",command=start_timer)
start.grid(row=2,column=0)
reset=Button(text="Reset",command = reset_timer)
reset.grid(row=2,column=2)
window.mainloop()