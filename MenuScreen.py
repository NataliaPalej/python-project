import tkinter as tk
from tkinter import *
from Team import Team
from random import randrange, choice
from PIL import ImageTk, Image
from DetailsScreen import DetailScreen
from TournamentScreen import TournamentScreen


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

team_list = [poland, bulgaria, croatia, germany, netherlands, hungary]


# tournament screen
def create_tournament():
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("600x600")
    window2.title("Tournament")
    Myapp2 = TournamentScreen(window2, teams)

# details screen
def details_screen():
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("460x390")
    window2.title("Volleyball Matches")
    detail_screen = DetailScreen(window2, team_list)
    detail_screen.display(0)

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
tournament_button = tk.Button(text="Create Tournament", font=('Arial', 16, 'bold'), height=2, command=create_tournament)
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



window.mainloop()
