class Team:
    def __init__(self, association, country, squad, injury, cancelled):
        self.__association = association
        self.__country = country
        self.__squad = squad
        self.__score = 0
        self.__played = 0
        self.__wins = 0
        self.__draws = 0
        self.__losses = 0
        self.__injury = injury
        self.__cancelled = cancelled

    def reset_all(self):
        self.__score = 0
        self.__played = 0
        self.__wins = 0
        self.__losses = 0
        self.__draws = 0
        self.__injury = False
        self.__cancelled = 0

    def get_country(self):
        return self.__country

    def get_squad(self):
        return self.__squad

    def get_association(self):
        return self.__association

    def get_score(self):
        return self.__score

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

    def get_percent_loss(self):
        if self.__played == 0:
            return 0
        else:
            return int(100 * (self.__losses / self.__played))

    def mark_win(self, score):
        self.__played += 1
        self.__wins += 1
        self.__score += score

    def mark_draw(self, score):
        self.__played += 1
        self.__draws += 1
        self.__score += score

    def mark_loss(self, score):
        self.__played += 1
        self.__losses += 1
        self.__score += score

    def mark_cancelled(self):
        self.__cancelled += 1
