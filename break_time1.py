from tkinter import *
import math

# สีตัวอักษรและสีพื้นหลัง
PINK = "#FF6699"
RED = "#FF0033"
PURPLE = "#660099"
GREEN = "#66FFCC"
# ชื่อfont
FONT_NAME = "Courier"
# เวลาทำงาน
WORK_MIN = 5
# เวลาเบรก
SHORT_BREAK_MIN = 5
# ระยะเวลาในการเบรก
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET (ตั้งเวลาใหม่อีกครั้ง)
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00.00")
    title_label.config(text="Timer")

# TIMER MECHANISM (จับเวลา)
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# COUNTDOWN MECHANISM (นับถอยหลัง)
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        maks = ""
        works_sessions = math.floor(reps/2)
        for _ in range(works_sessions):
            maks += "✅"
        check_marks.config(text=maks)

# UI SETUP ตั้งค่า
window = Tk()
window.title("เวลาพักเบรก")
window.config(padx=100, pady=50, bg=PURPLE, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, bg=PURPLE, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224)
orange_img = PhotoImage(file="orange.png")
canvas.create_image(100, 112, image=orange_img)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=PURPLE, font=(FONT_NAME,30))
check_marks.grid(column=1, row=3)

window.mainloop()