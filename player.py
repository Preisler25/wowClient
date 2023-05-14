class Player:
    def __init__(self, username, password, email, best_time, last_time, games_played, miss_clicked):
        self.username = username
        self.password = password
        self.email = email
        self.best_time = best_time
        self.last_time = last_time
        self.games_played = games_played
        self.miss_clicked = miss_clicked

    def __str__(self):
        return f"{self.username} {self.password} {self.email} {self.best_time} {self.last_time} {self.games_played} {self.miss_clicked}"

    def endGame(self):
        # testing for new best time
        if self.end_time < self.best_time:
            self.best_time = self.endTime
