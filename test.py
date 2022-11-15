# _author_ = "John Oakey"
# A Basic multi-screen demo
# PRELIMINARY HOUSE KEEPING

# only one of the following SHOULD be needed but testing cross platform
# indicates to me one works on windows and the other works on Debian (Unix)
import tkinter as tk
from tkinter import *
from NPalej_Details import Team
from random import randrange, choice

# I think it is a good practice to explicitly open a root screen
# This example shows how to get and utilize the full screen for your root example
window = tk.Tk()
window.configure(background='beige')
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


# I tested - window.wm_state('zoomed') - but for some reason it prevents top2 from being created
def create_tournament(teams):
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("600x600")
    window2.title("Tournament")
    Myapp2 = ScreenNo2(window2, teams)


# A couple of widgets I would not normally employ to demo where we are as tops are destroyed.
# our RootButton will call a simple exit function
def exit_app():
    exit()


# a lable and button to show we are down to the window
windowLabel = tk.Label(window, text=teams.keys(), font=('Arial', 12, 'bold'), takefocus=1, )
windowLabel.pack(pady=25, padx=25, ipadx=10, ipady=10, anchor="nw")
windowButton = tk.Button(text="Exit", font=('Arial', 16, 'bold'), command=exit_app)
windowButton.pack_configure(ipadx=10, ipady=10, padx=25, anchor="nw")

windowButton = tk.Button(text="Create Tournament", font=('Arial', 16, 'bold'), command=lambda: create_tournament(
    teams))  # NOTE called without parens = callbacks take no parameteres
windowButton.pack_configure(ipadx=10, ipady=10, padx=85, anchor="sw")


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








window.mainloop()
