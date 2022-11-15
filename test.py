import tkinter as tk
from tkinter import *
from Team import Team
from random import randrange, choice
from PIL import ImageTk, Image


window = tk.Tk()
window.configure(bg='beige')
window.title("Volleyball Matches")
window.geometry("600x600")

poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, False)
bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, True)
croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, False)
germany = Team("East German Volleyball Federation", "Germany", 11, False, False)
netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, False)
hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, True, True)

teams = {"Poland": poland, "Bulgaria": bulgaria, "Croatia": croatia, "Germany": germany,
         "Netherlands": netherlands, "Hungary": hungary}


# tournament screen
def create_tournament(teams):
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("600x600")
    window2.title("Tournament")
    Myapp2 = ScreenNo2(window2, teams)

# details screen
def details_screen():
    import detailsScreen


def exit_app():
    exit()

# blank line
labelBlank = Label(window, text=" ", height=4, bg="beige", font=("arial", 10, "bold"))
labelBlank.grid(row=1, column=0, sticky=W+E)
labelBlank.grid(row=2, column=0, sticky=W+E)

# team details button
teams_button = tk.Button(text="Team Details", font=('Arial', 16, 'bold'), height=2, width=5, takefocus=1, command=details_screen)
teams_button.grid(row=3, column=0, sticky=W+E, padx=180)

# blank line
labelBlank = Label(window, text=" ", height=4, bg="beige", font=("arial", 10, "bold"))
labelBlank.grid(row=4, column=0, sticky=W+E)
labelBlank.grid(row=5, column=0, sticky=W+E)

# tournament button
tournament_button = tk.Button(text="Create Tournament", font=('Arial', 16, 'bold'), height=2, command=lambda: create_tournament(teams))
tournament_button.grid(row=6, column=0, sticky=W+E, padx=180)

# blank line
labelBlank = Label(window, text=" ", height=4, bg="beige", font=("arial", 10, "bold"))
labelBlank.grid(row=7, column=0, sticky=W+E)
labelBlank.grid(row=8, column=0, sticky=W+E)

# exit button
exit_button = tk.Button(text="Exit", font=('Arial', 16, 'bold'), height=2, command=exit_app)
exit_button.grid(row=9, column=0, sticky=W+E, padx=180)



def get_random_teams(teams):
    team1 = choice(list(teams))
    team2 = choice(list(teams))
    print('{0} vs {1}'.format(team1, team2))
    while team1 == team2:
        team1 = choice(list(teams))
        team2 = choice(list(teams))
    return team1, team2

def mark_win():
    team.mark_win()

def mark_draw():
    team.mark_draw()

def mark_loss():
    team.mark_loss()


# Create a Secondary Screen for activity
class ScreenNo2:
    def __init__(self, window2, teams):
        team1, team2 = get_random_teams(teams)

        frame2 = tk.Frame(window2, width=500, height=500, bg="LightCyan2", pady=150)
        frame2.pack(side=LEFT)

        # First random country
        self.team1 = Button(frame2, text=team1, fg="black", font=("courier", 16, "bold"), state=DISABLED)
        self.team1.pack(side=LEFT, padx=20)

        # Second random country
        self.team2 = Button(frame2, text=team2, fg="black", font=("courier", 16, "bold"), state=DISABLED)
        self.team2.pack(side=LEFT, padx=20)

        self.team1.configure(height=2, width=20)
        self.team2.configure(height=2, width=20)

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


class detailsScreen:
    def __init__(self, window):
        # ===== GUI ===== #
        frame = Frame(window, width=200, height=200)
        frame.place(x=10, y=80)

        # title label
        self.label1 = Label(window, text="Volleyball Teams", fg="black", bg="pink", font=("arial", 16, "bold"))
        self.label1.place(x=140, y=30)  # place on screen

        # association
        self.association = Label(frame, text="Association", fg="black", width=15, font=("arial", 10, "bold"))
        self.association.grid(row=0, column=0, sticky=W + E)
        self.association_entry = Entry(frame)
        self.association_entry.insert(END, '')
        self.association_entry.grid(row=0, column=1, columnspan=3, sticky=W + E)

        # country
        self.country = Label(frame, text="Country", fg="black", width=15, font=("arial", 10, "bold"))
        self.country.grid(row=1, column=0, sticky=W + E)
        self.country_entry = Entry(frame)
        self.country_entry.insert(END, '')
        self.country_entry.grid(row=1, column=1, sticky=W + E)

        # placing first image on screen
        self.img = ImageTk.PhotoImage(Image.open("images/poland.jpg"))
        self.panel = tk.Label(window, image=self.img)
        self.panel.image = self.img
        self.panel.place(x=270, y=100)

        # squad
        self.squad = Label(frame, text="Squad", fg="black", width=15, font=("arial", 10, "bold"))
        self.squad.grid(row=2, column=0, sticky=W + E)
        self.squad_entry = Entry(frame)
        self.squad_entry.insert(END, '0')
        self.squad_entry.grid(row=2, column=1, sticky=W + E)

        # played
        self.played = Label(frame, text="Played", fg="black", width=15, font=("arial", 10, "bold"))
        self.played.grid(row=3, column=0, sticky=W + E)
        self.played_entry = Entry(frame)
        self.played_entry.insert(END, '0')
        self.played_entry.grid(row=3, column=1, sticky=W + E)

        # wins
        self.wins = Label(frame, text="Wins", fg="black", width=7, font=("arial", 10, "bold"))
        self.wins.grid(row=5, column=0)
        self.wins_entry = Entry(frame)
        self.wins_entry.insert(END, '0')
        self.wins_entry.grid(row=5, column=1)

        # losses
        self.losses = Label(frame, text="Losses", fg="black", width=7, font=("arial", 10, "bold"))
        self.losses.grid(row=5, column=2)
        self.losses_entry = Entry(frame)
        self.losses_entry.insert(END, '0')
        self.losses_entry.grid(row=5, column=3)

        # draws
        self.draws = Label(frame, text="Draws", fg="black", width=15, font=("arial", 10, "bold"))
        self.draws.grid(row=7, column=0, sticky=W + E)
        self.draws_entry = Entry(frame)
        self.draws_entry.insert(END, '0')
        self.draws_entry.grid(row=7, column=1, sticky=W + E, columnspan=4)

        # points
        self.points = Label(frame, text="Scores", fg="black", width=15, font=("arial", 10, "bold"))
        self.points.grid(row=8, column=0, sticky=W + E)
        self.points_entry = Entry(frame)
        self.points_entry.insert(END, '0')
        self.points_entry.grid(row=8, column=1, sticky=W + E)

        # checkbox
        # injury
        self.var_cb1 = IntVar()  # 0 unchecked, 1 checked
        self.cb1 = Checkbutton(frame, text="Injury", variable=self.var_cb1)
        self.cb1.grid(row=9, column=0, columnspan=1)

        # cancelled
        self.var_cb2 = IntVar()  # 0 unchecked, 1 checked
        self.cb2 = Checkbutton(frame, text="Cancelled", variable=self.var_cb2)
        self.cb2.grid(row=9, column=1, columnspan=1)

        # wins percentage
        self.win_percent_button = Button(frame, text="Wins %", fg="black", font=("arial", 10, "bold"), command=self.percent_win)
        self.win_percent_button.grid(row=10, column=0, sticky=W + E)

        self.wins_per = Entry(frame)
        self.wins_per.insert(END, '')
        self.wins_per.grid(row=10, column=1, sticky=E)

        # blank line
        self.labelBlank = Label(frame, text=" ", width=15, font=("arial", 10, "bold"))
        self.labelBlank.grid(row=14, column=0, columnspan=2, sticky=W + E)

        # reset
        self.reset = Button(frame, text="RESET", fg="black", font=("arial", 10, "bold"), command=self.reset_data)
        self.reset.grid(row=15, column=0, columnspan=4, sticky=W + E)

        # previous and next button
        self.previous = Button(frame, text="Previous", fg="black", font=("arial", 10, "bold"), command=self.next_button)
        self.previous.grid(row=16, column=0, columnspan=2, sticky=W + E)

        self.next_button = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=self.previous_button)
        self.next_button.grid(row=16, column=2, columnspan=2, sticky=W + E)

        # ===== TEAMS ===== #
        poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, False)
        bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, True)
        croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, False)
        germany = Team("East German Volleyball Federation", "Germany", 11, False, False)
        netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, False)
        hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, True, True)

        self.team_list = [poland, bulgaria, croatia, germany, netherlands, hungary]
        self.team = self.team_list[0]  # initialize to first match

    def display(self, index):
        global current
        global team
        team = team_list[index]
        current = index
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
        global current
        global team_list
        if current > 0:
            current -= 1
            self.display(current)

        if current == 0:
            img = ImageTk.PhotoImage(Image.open("images/poland.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 1:
            img = ImageTk.PhotoImage(Image.open("images/bulgaria.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 2:
            img = ImageTk.PhotoImage(Image.open("images/croatia.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 3:
            img = ImageTk.PhotoImage(Image.open("images/germany.jpg"))
            self.anel.configure(image=img)
            self.panel.image=img
        elif current == 4:
            img = ImageTk.PhotoImage(Image.open("images/netherlands.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 5:
            img = ImageTk.PhotoImage(Image.open("images/hungary.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img


    def previous_button(self):
        global current
        if current < (len(team_list) - 1):
            current += 1
            self.display(current)

        if current == 0:
            img = ImageTk.PhotoImage(Image.open("images/poland.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 1:
            img = ImageTk.PhotoImage(Image.open("images/bulgaria.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 2:
            img = ImageTk.PhotoImage(Image.open("images/croatia.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 3:
            img = ImageTk.PhotoImage(Image.open("images/germany.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 4:
            img = ImageTk.PhotoImage(Image.open("images/netherlands.jpg"))
            self.panel.configure(image=img)
            self.panel.image=img
        elif current == 5:
            img = ImageTk.PhotoImage(Image.open("images/hungary.jpg"))
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
        result = team.get_percent_win()
        self.wins_per.delete(0, END)
        self.wins_per.insert(END, (str(result) + " %"))


    def reset_data(self):
        global current
        team.reset_all()
        self.display(current)


window.mainloop()
