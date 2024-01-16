import random
import tkinter as tk
from tkinter import *

#dictionary
schema={
    "rock":{"rock":1,"paper":0,"scissor":2},
    "paper":{"rock":2,"paper":1,"scissor":0},
    "scissor":{"rock":0,"paper":2,"scissor":1}
}

comp_score=0
player_score=0

#Functions
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcome=["rock","paper","scissor"]
    random_number=random.randint(0,2)
    computer_choice=outcome[random_number]
    result    =schema[user_choice][computer_choice]
    
    
    player_choice_label.config(fg="red",text="Player Choice :"+str(user_choice))
    computer_choice_label.config(fg="green",text="Computer Choice : "+str(computer_choice))
    if result==2:
        player_score=player_score + 2
        player_score_label.config(text="Player : "+str(player_score))
        outcome_label.config(fg="blue",text="Outcome  : Player won")
    elif result==1 :
         player_score=player_score + 1
         comp_score = comp_score +1 
         player_score_label.config(text="Player : "+str(player_score))
         computer_score_label.config(text="Computer : "+str(comp_score))
         outcome_label.config(fg="blue",text="Outcome  : Draw")
    elif result==0:
        comp_score=comp_score+2
        computer_score_label.config(text="Computer : "+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome  :Computer won")
    
        
    

#main screen
root=Tk()
root.title("Rock-Paper-Scissor Game")


#labels
Label(root,text="Rock,Paper,Scissor",font=("calibri",14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(root,text="Please select an option", font=("calibri",12)).grid(row=1,sticky=N)
player_score_label=Label(root,text="Player : 0",font=("calibri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label=Label(root,text="Computer: 0",font=("calibri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label=Label(root,font=("Calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label=Label(root,font=("Calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label=Label(root,font=("Calibri",12))
outcome_label.grid(row=3,sticky=N)

# BUttons
Button(root,text="Rock",width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(root,text="Paper",width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,pady=5)
Button(root,text="Scissor",width=15,command=lambda:outcome_handler("scissor")).grid(row=4,sticky=E,padx=5,pady=5)

#Dummy label

Label(root).grid(row=5)







root.mainloop()
