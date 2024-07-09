import tkinter as tk
from PIL import ImageTk, Image
import random
import math

# Initialize Tkinter
root = tk.Tk()
root.title("Rock Paper Scissors")
root.attributes('-fullscreen', True)  # Set fullscreen mode

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((300, 300)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((300, 300)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((300, 300)))

# Background image
bg_img = ImageTk.PhotoImage(Image.open("circle_bg.jpeg").resize((root.winfo_screenwidth(), root.winfo_screenheight())))
background_label = tk.Label(root, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to determine winner
def determine_winner(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return player_choice, computer_choice

# Function to handle player choice
def handle_choice(choice):
    player_choice, computer_choice = determine_winner(choice)
    update_score(player_choice, computer_choice)

# Function to update scoreboard
def update_score(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        result_text = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_text = "You win!"
        player_score += 1
    else:
        result_text = "Computer wins!"
        computer_score += 1

    result_label.config(text=result_text)
    player_img.config(image=get_image(player_choice))
    computer_img.config(image=get_image(computer_choice))
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to get image based on choice
def get_image(choice):
    if choice == "rock":
        return rock_img
    elif choice == "paper":
        return paper_img
    elif choice == "scissors":
        return scissors_img

# Initialize scores
player_score = 0
computer_score = 0

# Images for player and computer
player_img = tk.Label(root, image=None)
player_img.place(x=root.winfo_screenwidth()//4, y=root.winfo_screenheight()//2, anchor="center")

computer_img = tk.Label(root, image=None)
computer_img.place(x=root.winfo_screenwidth()*3//4, y=root.winfo_screenheight()//2, anchor="center")

rock_btn = tk.Button(root, text="Rock", command=lambda: handle_choice("rock"), bg="violet", fg="black", width=15,height=3,font=("Helvetica", 25,),borderwidth=15)
rock_btn.place(x=root.winfo_screenwidth()//6, y=root.winfo_screenheight()*7//8,anchor="center")

paper_btn = tk.Button(root, text="Paper", command=lambda: handle_choice("paper"), bg="violet", fg="black", width=15,height=3,font=("Helvetica", 25),borderwidth=15)
paper_btn.place(x=root.winfo_screenwidth()//2, y=root.winfo_screenheight()*7//8,anchor="center")

scissors_btn = tk.Button(root, text="Scissors", command=lambda: handle_choice("scissors"), bg="violet", fg="black", width=15,height=3,font=("Helvetica", 25),borderwidth=15)
scissors_btn.place(x=root.winfo_screenwidth()*5//6, y=root.winfo_screenheight()*7//8,anchor="center")

# Result text
result_label = tk.Label(root, text="", font=("Helvetica", 25), bg="pink")
result_label.place(relx=0.5, rely=0.1, anchor="center")

# Scoreboard
player_score_label = tk.Label(root, text=f"Player Score: {player_score}", font=("Helvetica", 30),bg="pink")
player_score_label.place(x=50, y=50)

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=("Helvetica", 30), bg="pink")
computer_score_label.place(x=root.winfo_screenwidth()*3//4 + 50, y=50)

# Run the Tkinter event loop
root.mainloop()


