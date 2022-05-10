import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Reaction counter")
window.geometry("600x350")

time_1 = 0
time_2 = 0
pointless_click = 0
reaction = 0
col = str()


frame_2 = tk.Label(
    text = "pointless click amount : \n Your reaction :",
    width = 100,
    bg = "#34A2FE"
)

label = tk.Label(
    text = "Click START to start and then click STOP when you see red",
    bg = "green",
    fg = "black",
    width = 100,
    height = 12
)

frame = tk.Frame(
    height = 5
)


def your_stats():
    global  time_1,time_2,pointless_click
    reaction = round(time_2 - time_1,2)
    frame_2.config(text = f"pointless click amount : {pointless_click} \n Your reaction : {reaction}")
    time_1 = 0
    time_2 = 0

def red_click():
    if col == "red":
        global time_2
        time_2 = time.time()
        your_stats()
    else:
        global pointless_click
        pointless_click += 1

def color_change():
    global col,time_1
    colors = ["red","yellow","green","pink"]
    color = random.choice(colors)
    col = color
    if color == "red":
        time_1 = time.time()
    label.config(bg = color, text = "")
    window.after(random.randint(1000,4000),color_change)


def reaction_counter():
    window.after(random.randint(1000,2000),color_change)
    label.config(text = "")
    button.config(text = "STOP",command = red_click)


button = tk.Button(
    text = "START",
    bg = "red",
    fg = "black",
    width = 10,
    height = 1,
    command = reaction_counter
)

# frame = tk.Label(
#     text = "",
#     width = 600,
#     bg = "#34A2FE"
# )

for c in window.children:
    print(c)
    window.children[c].pack()
window.mainloop()