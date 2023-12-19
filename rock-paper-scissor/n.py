

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

player_score = 0
computer_score = 0

 # Creating the tuples of options
options = [('Rock', 0), ('Paper', 1), ('Scissor', 2)]



  
def open_game():
 # Initializing the scores of player and computer
 start_root.destroy()
 pygame.init()
 button_click_sound = pygame.mixer.Sound('click.wav')
 win_sound = pygame.mixer.Sound('win.wav')
 lose_sound=pygame.mixer.Sound('loses.wav')
 tie_sound=pygame.mixer.Sound('Draw.wav')
 


 # Function to stop the video

 def player_choice(player_input):
    global player_score, computer_score
    computer_input = get_computer_choice()

    player_choice_label.config(text='You Selected: ' + player_input[0])
    computer_choice_label.config(text='Computer Selected: ' + computer_input[0])

    # Update player and computer images based on their choices
    update_images(player_input[0], computer_input[0])
    button_click_sound.play()
    if player_input == computer_input:
        winner_img_label.config(image=draw_image_tk)
        win_sound.stop()
       
        lose_sound.stop()
        tie_sound.play()
    elif (player_input[1] - computer_input[1]) % 3 == 1:
        player_score += 1
        winner_img_label.config(image=win_image_tk)
        tie_sound.stop()
        lose_sound.stop()
        win_sound.play()

        player_score_label.config(text='Your Score: ' + str(player_score))
    
    else:
        computer_score += 1
        winner_img_label.config(image=lose_image_tk)
        win_sound.stop()
        tie_sound.stop()
        lose_sound.play()
        computer_score_label.config(text='Computer Score: ' + str(computer_score))
       
    if player_score == 5:
        messagebox.showinfo(message='CONGRATULATIONS! YOU ARE THE OVERALL CHAMPION OF THE GAME')
        
        disable_buttons()
    elif computer_score == 5:
        messagebox.showinfo(message='SORRY, COMPUTER IS THE OVERALL CHAMPION OF THE GAME')
        disable_buttons()

 # Function to get a random choice from the computer
 def get_computer_choice():
    return random.choice(options)

 # Function to disable the game buttons
 def disable_buttons():
    rock_btn.config(state=DISABLED)
    paper_btn.config(state=DISABLED)
    scissors_btn.config(state=DISABLED)

 # Function to reset the game
 def reset_game():
    button_click_sound.play()
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    winner_img_label.config(image=blank_img_tk)
    player_score_label.config(text='Your Score: 0')
    computer_score_label.config(text='Computer Score: 0')
    player_choice_label.config(text='You Selected: ---')
    computer_choice_label.config(text='Computer Selected: ---')

    # Reset player and computer images to default
    player_choice_img_label.config(image=blank_img_tk)
    computer_choice_img_label.config(image=blank_img_tk)

    rock_btn.config(state=NORMAL)
    paper_btn.config(state=NORMAL)
    scissors_btn.config(state=NORMAL)
  

 # Function to update the player and computer images based on their choices
 def update_images(player_choice, computer_choice):
    if player_choice == 'Rock':
        player_choice_img_label.config(image=rock_img_tk)
    elif player_choice == 'Paper':
        player_choice_img_label.config(image=paper_img_tk)
    elif player_choice == 'Scissor':
        player_choice_img_label.config(image=scissor_img_tk)

    if computer_choice == 'Rock':
        computer_choice_img_label.config(image=rock_img_tk)
    elif computer_choice == 'Paper':
        computer_choice_img_label.config(image=paper_img_tk)
    elif computer_choice == 'Scissor':
        computer_choice_img_label.config(image=scissor_img_tk)
        

  # Creating the window
 root = Tk()


 root.title("Rock Paper Scissors Game")
 root.geometry("1500x900")  # Set the root window to full screen
 background_img = Image.open("sk.jpg")
 background_img = background_img.resize((1700, 1000), Image.LANCZOS)
 background_img_tk = ImageTk.PhotoImage(background_img)
 background_label = Label(root, image=background_img_tk)
 background_label.place(x=0, y=0, relwidth=1, relheight=1)

 # Heading Label
 heading_label = Label(root, text="ROCK PAPER SCISSORS GAME", font=("Algerian", 28, "bold"), fg="green",bg="white")
 heading_label.pack(pady=20)



 # Load the rock, paper, and scissor images
 blank_img=Image.open("blank.png")
 rock_img = Image.open("rocks.png")
 paper_img = Image.open("papers.png")
 scissor_img = Image.open("scissors.png")

 # Resize the images
 blank_img = blank_img.resize((200, 200), Image.LANCZOS)
 rock_img = rock_img.resize((200, 200), Image.LANCZOS)
 paper_img = paper_img.resize((200, 200), Image.LANCZOS)
 scissor_img = scissor_img.resize((200, 200), Image.LANCZOS)

 # Convert the resized images to Tkinter-compatible format
 blank_img_tk =ImageTk.PhotoImage(blank_img)
 rock_img_tk = ImageTk.PhotoImage(rock_img)
 paper_img_tk = ImageTk.PhotoImage(paper_img)
 scissor_img_tk = ImageTk.PhotoImage(scissor_img)
 win_image = Image.open('win.png')
 win_image = win_image.resize((200, 200), Image.LANCZOS)
 win_image_tk = ImageTk.PhotoImage(win_image)

 lose_image = Image.open('loose.png')
 lose_image = lose_image.resize((200, 200), Image.LANCZOS)
 lose_image_tk = ImageTk.PhotoImage(lose_image)

 draw_image = Image.open('draw.png')
 draw_image =draw_image.resize((200, 200), Image.LANCZOS)
 draw_image_tk = ImageTk.PhotoImage(draw_image)
 
 # Frame for game widgets
 input_frame = Frame(root,bg="white")
 input_frame.pack()

 # Player options label
 player_options = Label(input_frame, text="Your Options:", font=("Arial", 19), fg="black",bg="white")
 player_options.grid(row=0, column=0, pady=10)

 # Game buttons
 rock_btn = Button(input_frame, text='Rock', width=20, bd=10, bg='#BBDEFB', font=("comicsans", 17, "bold"),fg="#000000", command=lambda: player_choice(options[0]))
 rock_btn.grid(row=1, column=1, padx=10, pady=5)

 paper_btn = Button(input_frame, text='Paper', width=20, bd=10, bg='#80CBC4', font=("comicsans", 17, "bold"),
                   command=lambda: player_choice(options[1]))
 paper_btn.grid(row=1, column=2, padx=10, pady=5)

 scissors_btn = Button(input_frame, text='Scissors', width=20, bd=10, bg='#FF8A65', font=("comicsans", 17, "bold"),
                      command=lambda: player_choice(options[2]))
 scissors_btn.grid(row=1, column=3, padx=10, pady=5)

 # Frame for result widgets
 result_frame = Frame(root,bg="white")
 result_frame.pack(pady=20)

 # Player and computer choice labels
 player_choice_label = Label(result_frame, text='You Selected: ---', font=("Arial", 19), fg="black",bg="white")
 player_choice_label.grid(row=0, column=0, padx=10,pady=10)

 computer_choice_label = Label(result_frame, text='Computer Selected: ---', font=("Arial", 19), fg="black",bg="white")
 computer_choice_label.grid(row=0, column=1, padx=10,pady=10)

 # Player and computer choice images
 player_choice_img_label = Label(result_frame, image=blank_img_tk)
 player_choice_img_label.grid(row=1, column=0, padx=5)

 computer_choice_img_label = Label(result_frame, image=blank_img_tk)
 computer_choice_img_label.grid(row=1, column=1, padx=5)
 winner_img_label = Label(result_frame, image=blank_img_tk)
 winner_img_label.grid(row=1, column=3, padx=5)
 # Score labels
 player_score_label = Label(result_frame, text='Your Score: 0', font=("Arial", 19), fg="black",bg="white")
 player_score_label.grid(row=2, column=0, padx=10, pady=10)

 computer_score_label = Label(result_frame, text='Computer Score: 0', font=("Arial", 19), fg="black",bg="white")
 computer_score_label.grid(row=2, column=1, padx=10, pady=10)

 # Reset button
 def end_game():
    button_click_sound.play()
    if messagebox.askyesno("Quit Game", "Are you sure you want to quit the game?"):
     root.destroy()
     
 reset_btn = Button(root, text="Reset", width=12, bd=5, bg="#90caf9", fg="#000000", font=("Arial", 19, "bold"),
command=reset_game)
 reset_btn.pack(pady=10)

 end_button = Button(root, text="Quit", width=12, bd=5, bg="#ef9a9a", fg="#000000", font=("Arial", 19, "bold"),
 command=end_game)
 end_button.pack(pady=10)
 # Run the GUI
 root.mainloop()
def play_click_sound():
    button_click_sound.play()
def open_tutorial():
    button_click_sound.play()
    tutorial_root = Tk()
    tutorial_root.title("Tutorial")
    tutorial_root.geometry("900x700")

    tutorial_text = "Tutorial\n\n1. Select either rock, paper, or scissors by clicking the corresponding button.\n\n2. The computer will also make its choice.\n\n3. The winner will be determined based on the following rules:\n\n- Rock beats scissors\n- Paper beats rock\n- Scissors beats paper\n\n4. The player and computer choices will be displayed.\n\n5. The scores will be updated accordingly.\n\n6. The first player to reach a score of 5 wins the game.\n\n7. Click the 'Reset' button to start a new game.\n\n8. Enjoy playing!"

    tutorial_label = Label(tutorial_root, text=tutorial_text, font=('Arial', 17))
    tutorial_label.pack(pady=20)

    tutorial_root.mainloop()
# Creating the window
start_root = Tk()
start_root.title("Rock Paper Scissors")
start_root.geometry("1500x900")
 # Set the root window to full screen
pygame.mixer.init()
button_click_sound = pygame.mixer.Sound('click.wav')

background_img = Image.open("st.jpg")
background_img = background_img.resize((1700, 1000), Image.LANCZOS)
background_img_tk = ImageTk.PhotoImage(background_img)

background_label = Label(start_root, image=background_img_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Creating the start button
def end_game():
        button_click_sound.play()
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit the game?"):
           start_root.destroy()





intro_button = Button(start_root, text="Start", width=12, bd=5, bg="red", fg="#000000", font=("Arial", 25, "bold"), command=lambda: [play_click_sound(), open_game()])
intro_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# Creating the tutorial button
tutorial_button = Button(start_root, text="Tutorial", width=12, bd=5, font=('Arial', 25, 'bold'), bg="green", fg="#000000", command=open_tutorial)
tutorial_button.place(relx=0.5, rely=0.8, anchor=CENTER)
end_button = Button(start_root, text="Quit", width=12, bd=5, bg="#18FFFF", fg="#000000", font=("Arial", 25, "bold"),
 command=end_game)
end_button.place(relx=0.5, rely=0.9, anchor=CENTER)
 # Run the GUI
start_root.mainloop()

