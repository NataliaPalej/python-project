from tkinter import *

from Team import Team

window = Tk()
window.geometry("500x450")
window.title("Volleyball Matches")

# Event Handling Methods
def display(index):
    global current
    global team
    team = team_list[index]
    current = index
    association_entry.delete(0, END)
    association_entry.insert(END, team.get_association())

    country_entry.delete(0, END)
    country_entry.insert(END, team.get_country())

    squad_entry.delete(0, END)
    squad_entry.insert(END, team.get_squad())

    played_entry.delete(0, END)
    played_entry.insert(END, team.get_played())

    wins_entry.delete(0, END)
    wins_entry.insert(END, team.get_wins())

    draws_entry.delete(0, END)
    draws_entry.insert(END, team.get_draws())

    losses_entry.delete(0, END)
    losses_entry.insert(END, team.get_losses())

    points_entry.delete(0, END)
    points_entry.insert(END, team.get_points())

    injury = team.get_injury()
    if injury == True:
        var_cb1.set(1)
    else:
        var_cb1.set(0)

    cancelled = team.get_cancelled()
    if cancelled == True:
        var_cb2.set(1)
    else:
        var_cb2.set(0)


def mark_win():
    team.mark_win()
    display(current)


def mark_draw():
    team.mark_draw()
    display(current)


def mark_loss():
    team.mark_loss()
    display(current)


def add_goals():
    goals = int(goals_number.get())
    team.add_goals(goals)
    display(current)


def percent_win():
    result = team.get_percent_win()
    wins_per.delete(0, END)
    wins_per.insert(END, (str(result) + " %"))


def reset_data():
    global current
    team.reset_all()
    display(current)


def next_button():
    global current
    if current > 0:
        current -= 1
        display(current)


def previous_button():
    global current
    if current < (len(team_list) - 1):
        current += 1
        display(current)


def insert_new_team():
    association1 = association_entry.get()
    country1 = country_entry.get()
    squad1 = squad_entry.get()

    injured = False
    if var_cb1.get() == 1:
        injured = True

    cancelled = False
    if var_cb2.get() == 1:
        cancelled = True

    new_team = Team(association1, country1, squad1, injured, cancelled)
    team_list.append(new_team)


def clear_data():
    association_entry.delete(0, END)
    country_entry.delete(0, END)
    squad_entry.delete(0, END)
    played_entry.delete(0, END)
    wins_entry.delete(0, END)
    losses_entry.delete(0, END)
    draws_entry.delete(0, END)
    wins_per.delete(0, END)
    var_cb1.set(0)
    var_cb2.set(0)
# ===== END OF METHOD DECLARATION ===== #


# ===== TEAMS ===== #
poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, False)
bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, True)
croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, False)
germany = Team("East German Volleyball Federation", "Germany", 11, False, False)
netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, False)
hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, True, True)

global team_list
team_list = [poland, bulgaria, croatia, germany, netherlands, hungary]
global current                  # current team
global team
team = team_list[0]             # initialize to first match
# ===== END OF TEAMS ===== #

# teams = {"poland": poland, "bulgaria": bulgaria}
#
# tournament_teams = [poland, bulgaria]
#
# def tournament_hadler(tournament_teams, winning_team, loosing_team):
#     for t in tournament_teams:
#         t.add_played()
#     winning_team.mark_win()
#     loosing_team.mark_loss()
#
# teams.get("poland").add_goals(1)


# ===== GUI ===== #
frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

# title label
label1 = Label(window, text="Volleyball Matches", fg="black", bg="pink", font=("arial", 16, "bold"))
label1.place(x=160, y=30)  # place on screen

# association
association = Label(frame, text="Association", fg="black", width=15, font=("arial", 10, "bold"))
association.grid(row=0, column=0, sticky=W+E)
association_entry = Entry(frame)
association_entry.insert(END, '')
association_entry.grid(row=0, column=1, columnspan=3, sticky=W+E)

# country
country = Label(frame, text="Country", fg="black", width=15, font=("arial", 10, "bold"))
country.grid(row=1, column=0, sticky=W+E)
country_entry = Entry(frame)
country_entry.insert(END, '')
country_entry.grid(row=1, column=1, sticky=W+E)

# add country picture column=2

# squad
squad = Label(frame, text="Squad", fg="black", width=15, font=("arial", 10, "bold"))
squad.grid(row=2, column=0, sticky=W+E)
squad_entry = Entry(frame)
squad_entry.insert(END, '0')
squad_entry.grid(row=2, column=1, sticky=W+E)

# played
played = Label(frame, text="Played", fg="black", width=15, font=("arial", 10, "bold"))
played.grid(row=3, column=0, sticky=W + E)
played_entry = Entry(frame)
played_entry.insert(END, '0')
played_entry.grid(row=3, column=1, sticky=W+E)

# wins
wins = Label(frame, text="Wins", fg="black", width=7, font=("arial", 10, "bold"))
wins.grid(row=5, column=0)
wins_entry = Entry(frame)
wins_entry.insert(END, '0')
wins_entry.grid(row=5, column=1)

# losses
losses = Label(frame, text="Losses", fg="black", width=7, font=("arial", 10, "bold"))
losses.grid(row=5, column=2)
losses_entry = Entry(frame)
losses_entry.insert(END, '0')
losses_entry.grid(row=5, column=3)

# draws
draws = Label(frame, text="Draws", fg="black", width=15, font=("arial", 10, "bold"))
draws.grid(row=7, column=0, sticky=W+E)
draws_entry = Entry(frame)
draws_entry.insert(END, '0')
draws_entry.grid(row=7, column=1, sticky=W+E)

# points
points = Label(frame, text="Scores", fg="black", width=15, font=("arial", 10, "bold"))
points.grid(row=8, column=0, sticky=W + E)
points_entry = Entry(frame)
points_entry.insert(END, '0')
points_entry.grid(row=8, column=1, sticky=W+E)

# checkbox
# injury
var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Injury", variable=var_cb1)
cb1.grid(row=9, column=0, columnspan=1)

# cancelled
var_cb2 = IntVar()  # 0 unchecked, 1 checked
cb2 = Checkbutton(frame, text="Cancelled", variable=var_cb2)
cb2.grid(row=9, column=1, columnspan=1)

# ===== BUTTONS ===== #
# add win
button1 = Button(frame, text="Add Win", fg="black", font=("arial", 10, "bold"), command=mark_win)
button1.grid(row=10, column=0, sticky=W+E)

# add loss
button3 = Button(frame, text="Add Loss", fg="black", font=("arial", 10, "bold"), command=mark_loss)
button3.grid(row=10, column=1, sticky=W+E)

# add draw
button2 = Button(frame, text="Add Draw", fg="black", font=("arial", 10, "bold"), command=mark_draw)
button2.grid(row=10, column=2, sticky=W+E)

# wins percentage
win_percent_button = Button(frame, text="Wins %", fg="black", font=("arial", 10, "bold"), command=percent_win)
win_percent_button.grid(row=12, column=0, sticky=W+E)

wins_per = Entry(frame)
wins_per.insert(END, '')
wins_per.grid(row=12, column=1, sticky=E)

# scores button
scores_button = Button(frame, text="Add Scores", fg="black", font=("arial", 10, "bold"), command=add_goals)
scores_button.grid(row=13, column=0, sticky=W + E)

# scores list
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
goals_number = StringVar()
combo1 = OptionMenu(frame, goals_number, *list1)
goals_number.set("1")
combo1.grid(row=13, column=1, sticky=W+E)

# blank line
labelBlank = Label(frame, text=" ", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=14, column=0, columnspan=2, sticky=W+E)

# reset
reset = Button(frame, text="RESET", fg="black", font=("arial", 10, "bold"), command=reset_data)
reset.grid(row=15, column=0, columnspan=4, sticky=W+E)

# previous and next button
previous = Button(frame, text="Previous", fg="black", font=("arial", 10, "bold"), command=next_button)
previous.grid(row=16, column=0, columnspan=2, sticky=W+E)

next_button = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=previous_button)
next_button.grid(row=16, column=2, columnspan=2, sticky=W+E)

display(0)

mainloop()
