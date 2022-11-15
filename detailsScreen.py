from tkinter import *
from PIL import ImageTk, Image

from NPalej_Details import Team

window = Tk()
window.geometry("460x390")
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
    if injury:
        var_cb1.set(1)
    else:
        var_cb1.set(0)

    cancelled = team.get_cancelled()
    if cancelled:
        var_cb2.set(1)
    else:
        var_cb2.set(0)


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


def percent_win():
    result = team.get_percent_win()
    wins_per.delete(0, END)
    wins_per.insert(END, (str(result) + " %"))


def reset_data():
    global current
    team.reset_all()
    display(current)


# change picture method
#def change_pic():
    #photo1 = ImageTk.PhotoImage(Image.open("\\images\\poland.jpg"))
    #labelname.configure(image=photo1)
    #print("updated")
    #window.update()


# ===== TEAMS ===== #
poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, False)
bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, True)
croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, False)
germany = Team("East German Volleyball Federation", "Germany", 11, False, False)
netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, False)
hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, True, True)

global team_list
team_list = [poland, bulgaria, croatia, germany, netherlands, hungary]
global current          # current team
global team
team = team_list[0]     # initialize to first match

# ===== GUI ===== #
frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

# title label
label1 = Label(window, text="Volleyball Teams", fg="black", bg="pink", font=("arial", 16, "bold"))
label1.place(x=140, y=30)  # place on screen

# association
association = Label(frame, text="Association", fg="black", width=15, font=("arial", 10, "bold"))
association.grid(row=0, column=0, sticky=W + E)
association_entry = Entry(frame)
association_entry.insert(END, '')
association_entry.grid(row=0, column=1, columnspan=3, sticky=W + E)

# country
country = Label(frame, text="Country", fg="black", width=15, font=("arial", 10, "bold"))
country.grid(row=1, column=0, sticky=W + E)
country_entry = Entry(frame)
country_entry.insert(END, '')
country_entry.grid(row=1, column=1, sticky=W + E)

# creating canvas to place flag image
canvas = Canvas(window, width=200, height=55)
canvas.place(x=270, y=104)
canvas.create_image(45, 30, anchor=CENTER)

# Poland flag
img = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\poland.jpg")
canvas.create_image(45, 30, anchor=CENTER, image=img)

# bulgaria flag
img2 = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\bulgaria.png")
#canvas.create_image(30, 30, anchor=CENTER, image=img2)

# croatia flag
img3 = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\croatia.png")
#canvas.create_image(30, 30, anchor=CENTER, image=img3)

# germany flag
img4 = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\germany.png")
#canvas.create_image(30, 30, anchor=CENTER, image=img4)

# netherlands flag
img5 = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\netherlands.png")
#canvas.create_image(30, 30, anchor=CENTER, image=img5)

# hungary flag
img6 = PhotoImage(file="C:\\Users\\Natalia\\Desktop\\Software Design with AI in Cloud\\Year_2\\software-"
                      "dev-cloud\\python-project\\images\\hungary.png")
#canvas.create_image(30, 30, anchor=CENTER, image=img6)

#flags = [img, img2, img3, img4, img5, img6]

# squad
squad = Label(frame, text="Squad", fg="black", width=15, font=("arial", 10, "bold"))
squad.grid(row=2, column=0, sticky=W + E)
squad_entry = Entry(frame)
squad_entry.insert(END, '0')
squad_entry.grid(row=2, column=1, sticky=W + E)

# played
played = Label(frame, text="Played", fg="black", width=15, font=("arial", 10, "bold"))
played.grid(row=3, column=0, sticky=W + E)
played_entry = Entry(frame)
played_entry.insert(END, '0')
played_entry.grid(row=3, column=1, sticky=W + E)

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
draws.grid(row=7, column=0, sticky=W + E)
draws_entry = Entry(frame)
draws_entry.insert(END, '0')
draws_entry.grid(row=7, column=1, sticky=W + E, columnspan=4)

# points
points = Label(frame, text="Scores", fg="black", width=15, font=("arial", 10, "bold"))
points.grid(row=8, column=0, sticky=W + E)
points_entry = Entry(frame)
points_entry.insert(END, '0')
points_entry.grid(row=8, column=1, sticky=W + E)

# checkbox
# injury
var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Injury", variable=var_cb1)
cb1.grid(row=9, column=0, columnspan=1)

# cancelled
var_cb2 = IntVar()  # 0 unchecked, 1 checked
cb2 = Checkbutton(frame, text="Cancelled", variable=var_cb2)
cb2.grid(row=9, column=1, columnspan=1)

# wins percentage
win_percent_button = Button(frame, text="Wins %", fg="black", font=("arial", 10, "bold"), command=percent_win)
win_percent_button.grid(row=10, column=0, sticky=W + E)

wins_per = Entry(frame)
wins_per.insert(END, '')
wins_per.grid(row=10, column=1, sticky=E)

# blank line
labelBlank = Label(frame, text=" ", width=15, font=("arial", 10, "bold"))
labelBlank.grid(row=14, column=0, columnspan=2, sticky=W + E)

# reset
reset = Button(frame, text="RESET", fg="black", font=("arial", 10, "bold"), command=reset_data)
reset.grid(row=15, column=0, columnspan=4, sticky=W + E)

# previous and next button
previous = Button(frame, text="Previous", fg="black", font=("arial", 10, "bold"), command=next_button)
previous.grid(row=16, column=0, columnspan=2, sticky=W + E)

next_button = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=previous_button)
next_button.grid(row=16, column=2, columnspan=2, sticky=W + E)

display(0)

mainloop()
