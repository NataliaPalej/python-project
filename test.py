#_author_ = "John Oakey"
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
root=tk.Tk()
root.configure(background='beige')
root.title("Rooty Tooty Root Screen")
root.geometry("600x600")

poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, False)
bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, True)
croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, False)
germany = Team("East German Volleyball Federation", "Germany", 11, False, False)
netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, False)
hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, True, True)

teams = {"poland": poland, "bulgaria": bulgaria, "croatia": croatia, "germany": germany, "netherlands": netherlands, "hungary": hungary}

# I tested - root.wm_state('zoomed') - but for some reason it prevents top2 from being created
def create_tournament(teams):
    top2 = Toplevel(root, bg="grey85")
    top2.geometry("600x600")
    top2.title("Top 2 Window")
    Myapp2=ScreenNo2(top2, teams)


# A couple of widgets I would not normally employ to demo where we are as tops are destroyed.
# our RootButton will call a simple exit function
def Fini():
    exit()
# a lable and button to show we are down to the root
RootLabel = tk.Label(root,text=teams.keys(), font=('Arial',12,'bold'), takefocus=1)
RootLabel.pack(pady=25, padx=25, ipadx=10, ipady=10, anchor="nw")
RootButton= tk.Button(text = "Exit", font=('Arial',16,'bold'), command=Fini) #NOTE called without parens = callbacks take no parameteres
RootButton.pack_configure(ipadx=10, ipady=10, padx=25, anchor="nw")

RootButton= tk.Button(text = "Create Tournament", font=('Arial',16,'bold'), command=lambda: create_tournament(teams)) #NOTE called without parens = callbacks take no parameteres
RootButton.pack_configure(ipadx=10, ipady=10, padx=85, anchor="sw")

#Create a Secondary Screen for activity
class ScreenNo2:
    def __init__(self, top2, teams):
        team1, team2 = self.get_random_teams(teams)

        frame2=tk.Frame(top2, width=scrW-300, height=scrH-400, bg="LightCyan2", pady=150)
        frame2.pack(side=LEFT)

        self.button2=Button(frame2, text=team1, fg="maroon", command=top2.destroy, font=("courier", 16, "bold"))
        # could close the whole shebang by using root.destroy instead of top2.destroy
        self.button2.pack(side=LEFT, padx=20)

        self.MoreMsg = Button(frame2, text=team2, fg="blue", command=self.write_message2, font=("arial", 16, "bold"))
        self.MoreMsg.pack(side=LEFT)

        self.button2.configure(height=2, width=20)
        self.MoreMsg.configure(height=2, width=20)


    def write_message2(self):
        print(teams) #sent to standard out & will duplicate multiple presses- not sent to GUI
        self.anotherLabel.pack(anchor ='nw', padx=20, side = BOTTOM)  # GUI display, will not be duplicated with multiple presses
        self.anotherLabel.configure(bg = 'cyan')

    def get_random_teams(self, teams):
        team1 = choice(list(teams))
        team2 = choice(list(teams))
        print(team1)
        print(team2)
        while team1 == team2:
            team1 = choice(list(teams))
            team2 = choice(list(teams))
        return team1, team2


root.mainloop()