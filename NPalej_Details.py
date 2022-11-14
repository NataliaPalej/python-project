class Team:
    def __init__(self, association, country, squad, injury, cancelled):
        self.__association = association
        self.__country = country
        self.__squad = squad
        self.__points = 0
        self.__played = 0
        self.__wins = 0
        self.__draws = 0
        self.__losses = 0
        self.__injury = injury
        self.__cancelled = cancelled

    def reset_all(self):
        self.__points = 0
        self.__played = 0
        self.__wins = 0
        self.__losses = 0
        self.__draws = 0

    def add_goals(self, points):
        self.__points += points

    def get_goals(self):
        return self.__goals

    def get_squad(self):
        return self.__squad

    def get_association(self):
        return self.__association

    def get_country(self):
        return self.__country

    def get_points(self):
        return self.__points

    def get_played(self):
        return self.__played

    def add_played(self):
        self.__played += 1

    def get_wins(self):
        return self.__wins

    def get_draws(self):
        return self.__draws

    def get_losses(self):
        return self.__losses

    def get_injury(self):
        return self.__injury

    def get_cancelled(self):
        return self.__cancelled

    def get_percent_win(self):
        if self.__played == 0:
            return 0
        else:
            return int(100 * (self.__wins / self.__played))

    def mark_win(self):
        self.__played += 1
        self.__wins += 1
        self.__points += 2

    def mark_draw(self):
        self.__played += 1
        self.__draws += 1
        self.__points += 1

    def mark_loss(self):
        self.__played += 1
        self.__losses += 1
