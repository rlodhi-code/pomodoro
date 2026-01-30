from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
timer = None

# ---------------------------- TIMER START ------------------------------- #
def start_timer():
    # For testing — start with 5 seconds
    # In real Pomodoro: count_down(WORK_MIN * 60)
    count_down(5)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    # Cancel any running timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None

    # Reset display
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    # Convert count (in seconds) to minutes and seconds
    minutes = count // 60
    seconds = count % 60

    # Format as MM:SS (always show two digits)
    time_text = f"{minutes:02d}:{seconds:02d}"

    # Update the text on the canvas
    canvas.itemconfig(timer_text, text=time_text)

    if count > 0:
        # Schedule the next call after 1000ms (1 second)
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Timer has finished — you can add sound, change color, start next phase, etc.
        print("Time's up!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro (tomato)")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

count_down(5 * 60)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="✔️", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
