from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import choice

class TournamentScreen:
    def __init__(self, window2, teams):
        team1, team2 = self.get_random_teams(teams)

        frame2 = tk.Frame(window2, width=500, height=500, bg="LightCyan2", pady=150)
        frame2.pack(side=LEFT)


        # First random country
        self.team1_button = Button(frame2, text=team1, fg="black", font=("courier", 16, "bold"), state=DISABLED)
        self.team1_button.pack(side=LEFT, padx=20)

        # Second random country
        self.team2_button = Button(frame2, text=team2, fg="black", font=("courier", 16, "bold"), state=DISABLED)
        self.team2_button.pack(side=LEFT, padx=20)

        self.team1_button.configure(height=2, width=20)
        self.team2_button.configure(height=2, width=20)

        # placing first image on screen
        self.img = ImageTk.PhotoImage(Image.open("images/"+team1.lower()+".jpg"))
        self.panel = tk.Label(window2, image=self.img)
        self.panel.image = self.img
        self.panel.place(x=170, y=100)

        self.img2 = ImageTk.PhotoImage(Image.open("images/"+team2.lower()+".jpg"))
        self.panel = tk.Label(window2, image=self.img2)
        self.panel.image = self.img2
        self.panel.place(x=370, y=100)

        # ===== BUTTONS ===== #
        # add win
        self.button1 = Button(frame2, text="Add Win", fg="black", font=("arial", 14, "bold"), command="")
        self.button1.configure(height=1, width=20)

        # add loss
        self.button3 = Button(frame2, text="Add Loss", fg="black", font=("arial", 10, "bold"), command="")
        self.button3.configure(height=1, width=20)

        # add draw
        self.button2 = Button(frame2, text="Add Draw", fg="black", font=("arial", 10, "bold"), command="")
        self.button2.configure(height=1, width=20)

    def write_message2(self):
        self.anotherLabel.pack(anchor='nw', padx=20, side=BOTTOM) # GUI display, will not be duplicated with multiple presses
        self.anotherLabel.configure(bg='cyan')


    def get_random_teams(self, teams):
        team1 = choice(list(teams))
        team2 = choice(list(teams))
        print('{0} vs {1}'.format(team1, team2))
        while team1 == team2:
            team1 = choice(list(teams))
            team2 = choice(list(teams))
        return team1, team2