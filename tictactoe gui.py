from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("319x363")
root.title("Tic Tac Toe - Aniket")
root.resizable(False, False)

# Game state variables
clicked = True  # True = X's turn, False = O's turn
count = 0       # Move counter

# Reset the game board
def reset():
    global clicked, count, winner
    clicked = True
    count = 0
    winner = False

    for btn in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        btn.config(text=" ", state=NORMAL, bg="SystemButtonFace")

# Disable all buttons
def disable_all_buttons():
    for btn in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        btn.config(state=DISABLED)

# Check for winner
def checkiwon():
    global winner
    winner = False

    combos = [
        (b1, b2, b3),
        (b4, b5, b6),
        (b7, b8, b9),
        (b1, b4, b7),
        (b2, b5, b8),
        (b3, b6, b9),
        (b1, b5, b9),
        (b3, b5, b7),
    ]

    for a, b, c in combos:
        if a["text"] == b["text"] == c["text"] != " ":
            a.config(bg="red")
            b.config(bg="red")
            c.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {a['text']} Wins!!")
            disable_all_buttons()
            return

    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        disable_all_buttons()

# Button click handler
def b_click(b):
    global clicked, count

    if b["text"] == " ":
        if clicked:
            b["text"] = "X"
            clicked = False
        else:
            b["text"] = "O"
            clicked = True
        count += 1
        checkiwon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box is already selected.\nChoose another.")

# Create buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

# Grid layout
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Menu bar
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
options_menu.add_command(label="Exit Game", command=root.quit)

# Start game
reset()
root.mainloop()
