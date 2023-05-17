class Player:
    def __init__(self, username, password, email, best_time, end_time, games_played, missed_clicks):
        self.username = username
        self.password = password
        self.email = email
        self.best_time = best_time
        self.end_time = end_time
        self.games_played = games_played
        self.missed_clicks = missed_clicks

    def __str__(self):
        return f"username: {self.username}\npassword: {self.password}\nemail: {self.email}\nbest_time: {self.best_time}\nend_time: {self.end_time}\ngames_played: {self.games_played}\nmiss_clicked: {self.missed_clicks}"

    def endGame(self):
        # testing for new best time
        if self.end_time < self.best_time:
            self.best_time = self.end_time
