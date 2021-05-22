from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#fe7171"
RED = "#ffaaa7"
TEAL = "#5c969e"
BLUE = "#0061a8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"
reps = 0
pomodoro_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(pomodoro_timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=BLUE)
        reps += 1
    elif reps % 2 == 0:
        count_down(break_sec)
        timer_label.config(text="Break", fg=PINK)
        reps += 1
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global pomodoro_timer
        pomodoro_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += check_mark
        check_label.config(text=marks, bg=TEAL, fg=BLUE, font=(FONT_NAME, 12, "normal"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=TEAL)


canvas = Canvas(width=200, height=224, bg=TEAL, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", bg=TEAL, fg=RED, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", fg=BLUE, font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", fg=BLUE, font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

check_label = Label(bg=TEAL)
check_label.grid(column=2, row=4)


window.mainloop()
