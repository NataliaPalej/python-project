from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


class DetailScreen:
    def __init__(self, window2, teams):
        self.team_list = teams
        self.current = 0  # current team
        self.team = self.team_list[0]  # initialize to first match

        # ===== GUI ===== #
        self.frame = tk.Frame(window2, width=200, height=200)
        self.frame.place(x=10, y=80)

        # title label
        self.label1 = Label(window2, text="Volleyball Teams", fg="black", bg="pink", font=("arial", 16, "bold"))
        self.label1.place(x=140, y=30)  # place on screen

        # association
        self.association = Label(self.frame, text="Association", fg="black", width=15, font=("arial", 10, "bold"))
        self.association.grid(row=0, column=0, sticky=W + E)
        self.association_entry = Entry(self.frame)
        self.association_entry.insert(END, '')
        self.association_entry.grid(row=0, column=1, columnspan=3, sticky=W + E)

        # country
        self.country = Label(self.frame, text="Country", fg="black", width=15, font=("arial", 10, "bold"))
        self.country.grid(row=1, column=0, sticky=W + E)
        self.country_entry = Entry(self.frame)
        self.country_entry.insert(END, '')
        self.country_entry.grid(row=1, column=1, sticky=W + E)

        # placing first image on screen
        self.img = ImageTk.PhotoImage(Image.open("images/poland.jpg"))
        self.panel = tk.Label(window2, image=self.img)
        self.panel.image = self.img
        self.panel.place(x=270, y=100)

        # squad
        self.squad = Label(self.frame, text="Squad", fg="black", width=15, font=("arial", 10, "bold"))
        self.squad.grid(row=2, column=0, sticky=W + E)
        self.squad_entry = Entry(self.frame)
        self.squad_entry.insert(END, '0')
        self.squad_entry.grid(row=2, column=1, sticky=W + E)

        # played
        self.played = Label(self.frame, text="Played", fg="black", width=15, font=("arial", 10, "bold"))
        self.played.grid(row=3, column=0, sticky=W + E)
        self.played_entry = Entry(self.frame)
        self.played_entry.insert(END, '0')
        self.played_entry.grid(row=3, column=1, sticky=W + E)

        # wins
        self.wins = Label(self.frame, text="Wins", fg="black", width=7, font=("arial", 10, "bold"))
        self.wins.grid(row=5, column=0)
        self.wins_entry = Entry(self.frame)
        self.wins_entry.insert(END, '0')
        self.wins_entry.grid(row=5, column=1)

        # losses
        self.losses = Label(self.frame, text="Losses", fg="black", width=7, font=("arial", 10, "bold"))
        self.losses.grid(row=5, column=2)
        self.losses_entry = Entry(self.frame)
        self.losses_entry.insert(END, '0')
        self.losses_entry.grid(row=5, column=3)

        # draws
        self.draws = Label(self.frame, text="Draws", fg="black", width=15, font=("arial", 10, "bold"))
        self.draws.grid(row=7, column=0, sticky=W + E)
        self.draws_entry = Entry(self.frame)
        self.draws_entry.insert(END, '0')
        self.draws_entry.grid(row=7, column=1, sticky=W + E, columnspan=4)

        # points
        self.points = Label(self.frame, text="Scores", fg="black", width=15, font=("arial", 10, "bold"))
        self.points.grid(row=8, column=0, sticky=W + E)
        self.points_entry = Entry(self.frame)
        self.points_entry.insert(END, '0')
        self.points_entry.grid(row=8, column=1, sticky=W + E)

        # checkbox
        # injury
        self.var_cb1 = IntVar()  # 0 unchecked, 1 checked
        self.cb1 = Checkbutton(self.frame, text="Injury", variable=self.var_cb1)
        self.cb1.grid(row=9, column=0, columnspan=1)

        # cancelled
        self.var_cb2 = IntVar()  # 0 unchecked, 1 checked
        self.cb2 = Checkbutton(self.frame, text="Cancelled", variable=self.var_cb2)
        self.cb2.grid(row=9, column=1, columnspan=1)

        # wins percentage
        self.win_percent_button = Button(self.frame, text="Wins %", fg="black", font=("arial", 10, "bold"), command=self.percent_win)
        self.win_percent_button.grid(row=10, column=0, sticky=W + E)

        self.wins_per = Entry(self.frame)
        self.wins_per.insert(END, '')
        self.wins_per.grid(row=10, column=1, sticky=E)

        # blank line
        self.labelBlank = Label(self.frame, text=" ", width=15, font=("arial", 10, "bold"))
        self.labelBlank.grid(row=14, column=0, columnspan=2, sticky=W + E)

        # reset
        self.reset = Button(self.frame, text="RESET", fg="black", font=("arial", 10, "bold"), command=self.reset_data)
        self.reset.grid(row=15, column=0, columnspan=4, sticky=W + E)

        # previous and next button
        self.previous = Button(self.frame, text="Previous", fg="black", font=("arial", 10, "bold"), command=self.previous_button)
        self.previous.grid(row=16, column=0, columnspan=2, sticky=W + E)

        self.next_button = Button(self.frame, text="Next", fg="black", font=("arial", 10, "bold"), command=self.next_button)
        self.next_button.grid(row=16, column=2, columnspan=2, sticky=W + E)



    # Event Handling Methods
    def display(self, index):
        self.current = index
        team = self.team_list[index]
        self.association_entry.delete(0, END)
        self.association_entry.insert(END, team.get_association())

        self.country_entry.delete(0, END)
        self.country_entry.insert(END, team.get_country())

        self.squad_entry.delete(0, END)
        self.squad_entry.insert(END, team.get_squad())

        self.played_entry.delete(0, END)
        self.played_entry.insert(END, team.get_played())

        self.wins_entry.delete(0, END)
        self.wins_entry.insert(END, team.get_wins())

        self.draws_entry.delete(0, END)
        self.draws_entry.insert(END, team.get_draws())

        self.losses_entry.delete(0, END)
        self.losses_entry.insert(END, team.get_losses())

        self.points_entry.delete(0, END)
        self.points_entry.insert(END, team.get_points())

        injury = team.get_injury()
        if injury:
            self.var_cb1.set(1)
        else:
            self.var_cb1.set(0)

        cancelled = team.get_cancelled()
        if cancelled:
            self.var_cb2.set(1)
        else:
            self.var_cb2.set(0)


    def next_button(self):
        if self.current < (len(self.team_list) - 1):
            self.current += 1
            self.display(self.current)

        team_name = self.team_list[self.current].get_country().lower()
        img = ImageTk.PhotoImage(Image.open("images/"+team_name+".jpg"))
        self.panel.configure(image=img)
        self.panel.image=img



    def previous_button(self):
        if self.current > 0:
            self.current -= 1
            self.display(self.current)

        team_name = self.team_list[self.current].get_country().lower()
        img = ImageTk.PhotoImage(Image.open("images/"+team_name+".jpg"))
        self.panel.configure(image=img)
        self.panel.image=img


    def clear_data(self):
        self.association_entry.delete(0, END)
        self.country_entry.delete(0, END)
        self.squad_entry.delete(0, END)
        self.played_entry.delete(0, END)
        self.wins_entry.delete(0, END)
        self.losses_entry.delete(0, END)
        self.draws_entry.delete(0, END)
        self.wins_per.delete(0, END)
        self.var_cb1.set(0)
        self.var_cb2.set(0)


    def percent_win(self):
        result = self.team.get_percent_win()
        self.wins_per.delete(0, END)
        self.wins_per.insert(END, (str(result) + " %"))


    def reset_data(self):
        self.team.reset_all()
        self.display(self.current)

