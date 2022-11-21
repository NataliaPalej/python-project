from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import choice


class TournamentScreen:
    def __init__(self, window2, teams):
        team1, team2 = self.get_random_teams(teams)

        frame2 = tk.Frame(window2, bg="grey85", pady=170)
        frame2.place(x=0, y=0)

        # disable window resize
        window2.resizable(False, False)

        # placing image on screen
        self.img = ImageTk.PhotoImage(Image.open("images/" + team1.lower() + ".jpg"))
        self.panel = tk.Label(frame2, image=self.img)
        self.panel.image = self.img
        self.panel.place(x=115, y=-110)

        self.img2 = ImageTk.PhotoImage(Image.open("images/" + team2.lower() + ".jpg"))
        self.panel = tk.Label(frame2, image=self.img2)
        self.panel.image = self.img2
        self.panel.place(x=390, y=-110)

        # vs label
        self.vs = Label(frame2, text="vs", fg="black", bg="grey85", font=("courier", 16, "bold"))
        self.vs.place(x=270, y=-95)

        # First random country
        self.team1_label = Label(frame2, text=team1, fg="black", font=("courier", 16, "bold"), borderwidth=1,
                                 relief="solid")
        self.team1_label.configure(height=2, width=20)
        self.team1_label.grid(column=2, row=0, padx=10)

        # Second random country
        self.team2_label = Label(frame2, text=team2, fg="black", font=("courier", 16, "bold"), borderwidth=1,
                                 relief="solid")
        self.team2_label.configure(height=2, width=20)
        self.team2_label.grid(column=3, row=0, padx=10, pady=5)

        # ===== BUTTONS ===== #
        # add score
        list1 = ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '23', '24', '25']
        score_team1 = StringVar()
        combo1 = OptionMenu(frame2, score_team1, *list1)
        score_team1.set("0")
        combo1.grid(column=1, columnspan=2, row=1)
        combo1.configure(borderwidth=1, relief="solid", width=5, height=2, bg="white")

        score_team2 = StringVar()
        combo2 = OptionMenu(frame2, score_team2, *list1)
        score_team2.set("0")
        combo2.grid(column=3, columnspan=2, row=1, pady=5)
        combo2.configure(borderwidth=1, relief="solid", width=5, height=2, bg="white")

        # submit tournament result
        self.button1 = Button(frame2, text="Submit", fg="black", bg="chartreuse3", font=("arial", 14, "bold"),
                              command=self.submit)
        self.button1.place(x=150, y=150)
        self.button1.configure(height=2, width=20)

        # add match cancelled
        self.button2 = Button(frame2, text="CANCELLED", fg="black", bg="brown1", font=("arial", 14, "bold"),
                              command=self.cancel)
        self.button2.place(x=150, y=220)
        self.button2.configure(width=20, height=2)

    # GUI display, will not be duplicated with multiple presses
    def write_message2(self):
        self.Label.pack(anchor='nw', padx=20, side=BOTTOM)
        self.Label.configure(bg='cyan')

    @staticmethod
    def get_random_teams(teams):
        team1 = choice(teams)
        team1 = team1.get_country()
        team2 = choice(teams)
        team2 = team2.get_country()
        print('{0} vs {1}'.format(team1, team2))
        while team1 == team2:
            team1 = choice(teams)
            team1 = team1.get_country()
            team2 = choice(teams)
            team2 = team2.get_country()
        return team1, team2

    def submit(self, score1, score2):
        # if score is the same, mark draw for both teams
        score1 = self.score_team1.get()
        score2 = self.score_team2.get()
        if score1 == score2:
            self.mark_draw()
        # if team1 has lower score than team2, mark loss to team1 and win to team2
        elif score1 < score2:
            self.mark_loss()
        # if team2 has bigger score than team2, mark win for team1 and loss for team2
        elif score1 > score2:
            self.mark_win()

    def cancel(self):
        self.canceled()
