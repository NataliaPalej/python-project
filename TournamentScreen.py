from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import choice


class TournamentScreen:
    def __init__(self, window2, teams):
        self.win = window2
        self.team1, self.team2, self.team1_obj, self.team2_obj = self.get_random_teams(teams)

        bg = ImageTk.PhotoImage(Image.open("images/tournament.jpg"))

        frame2 = tk.Frame(window2, pady=170)
        frame2.place(x=0, y=0)
        self.panel = tk.Label(frame2, image=bg)
        self.panel.image = bg
        self.panel.place(x=-330, y=-300)

        # disable window resize
        window2.resizable(False, False)

        # placing image on screen
        self.img = ImageTk.PhotoImage(Image.open("images/" + self.team1.lower() + ".jpg"))
        self.panel = tk.Label(frame2, image=self.img)
        self.panel.image = self.img
        self.panel.place(x=115, y=-110)

        self.img2 = ImageTk.PhotoImage(Image.open("images/" + self.team2.lower() + ".jpg"))
        self.panel = tk.Label(frame2, image=self.img2)
        self.panel.image = self.img2
        self.panel.place(x=390, y=-110)

        # vs label
        self.vs = Label(frame2, text="vs", fg="black", font=("courier", 16, "bold"))
        self.vs.place(x=270, y=-95)

        # First random country
        self.team1_label = Label(frame2, text=self.team1, fg="black", font=("courier", 16, "bold"), borderwidth=1,
                                 relief="solid")
        self.team1_label.configure(height=2, width=20)
        self.team1_label.grid(column=2, row=0, padx=10)

        # Second random country
        self.team2_label = Label(frame2, text=self.team2, fg="black", font=("courier", 16, "bold"), borderwidth=1,
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
                              command=lambda: self.submit(score_team1, score_team2))
        self.button1.place(x=150, y=150)
        self.button1.configure(height=2, width=20)

        # add match cancelled
        self.button2 = Button(frame2, text="CANCELLED", fg="black", bg="brown1", font=("arial", 14, "bold"),
                              command=self.cancel)
        self.button2.place(x=150, y=220)
        self.button2.configure(width=20, height=2)

    @staticmethod
    def get_random_teams(teams):
        team1 = choice(teams)
        team2 = choice(teams)
        team1_obj = team1
        team2_obj = team2
        team1 = team1.get_country()
        team2 = team2.get_country()
        while team1 == team2:
            team2 = choice(teams)
            team2 = team2.get_country()
        print('{0} vs {1}'.format(team1, team2))
        return team1, team2, team1_obj, team2_obj

    def submit(self, score1, score2):
        score1 = int(score1.get())
        score2 = int(score2.get())

        if score1 == score2:
            self.team1_obj.mark_draw(score1)
            self.team2_obj.mark_draw(score2)
        if int(score1) < int(score2):
            self.team2_obj.mark_win(score2)
            self.team1_obj.mark_loss(score1)
        elif int(score1) > int(score2):
            self.team1_obj.mark_win(score1)
            self.team2_obj.mark_loss(score2)

        self.exit()

    def cancel(self):
        self.team2_obj.mark_cancelled()
        self.team1_obj.mark_cancelled()
        self.exit()

    def exit(self):
        self.win.destroy()
