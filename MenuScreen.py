import tkinter as tk
from tkinter import *
from Team import Team
from DetailsScreen import DetailScreen
from TournamentScreen import TournamentScreen
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("600x600")
window.title("Volleyball Menu")
bg = ImageTk.PhotoImage(Image.open("images/volleyball.jpg"))
myBG = Label(image=bg)
myBG.place(x=0, y=0, relwidth=1, relheight=1)

window.resizable(False, False)

poland = Team("Polski Związek Piłki Siatkowej", "Poland", 14, False, 0)
bulgaria = Team("Bulgarian Volleyball Federation", "Bulgaria", 14, False, 0)
croatia = Team("Croatian Volleyball Federation", "Croatia", 14, False, 0)
germany = Team("East German Volleyball Federation", "Germany", 11, False, 0)
netherlands = Team("Nederlandse Volleybalbond", "Netherlands", 21, False, 0)
hungary = Team("Magyar Röplabda Szövetség", "Hungary", 18, False, 0)

team_list = [poland, bulgaria, croatia, germany, netherlands, hungary]


# tournament screen
def create_tournament():
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("570x500")
    window2.title("Tournament")
    TournamentScreen(window2, team_list)


# details screen
def details_screen():
    window2 = Toplevel(window, bg="grey85")
    window2.geometry("600x500")
    window2.title("Volleyball Teams")
    detail_screen = DetailScreen(window2, team_list)
    detail_screen.display(0)

    button = Button(window2, text="Close", width=100, height=2, command=window2.destroy, font=("arial", 10, "bold"))
    button.pack(side=tk.BOTTOM)


def exit_app():
    exit()


# team details button
teams_button = tk.Button(text="Team Details", font=('Arial', 16, 'bold'), height=2, width=15, takefocus=1,
                         command=details_screen)
teams_button.place(x=200, y=100)


# tournament button
tournament_button = tk.Button(text="Create Tournament", font=('Arial', 16, 'bold'), height=2, width=15,
                              command=create_tournament)
tournament_button.place(x=200, y=200)

# exit button
exit_button = tk.Button(text="Exit", width=15, font=('Arial', 16, 'bold'), height=2, command=exit_app,
                        bg="gray", fg="black")
exit_button.place(x=200, y=450)

window.mainloop()