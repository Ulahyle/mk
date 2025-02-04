class Team:
    teams = []

    def __init__(self, team_name):
        self.team_name = team_name
        self.points = 0
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        Team.teams.append(self)

    @staticmethod
    def validate_points(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if args[0].points < 0:
                args[0].points = 0
            return result
        return wrapper

    @validate_points
    def update_stats(self, result):
        if result == "win":
            self.points += 3
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        elif result == "draw":
            self.points += 1
            self.draws += 1
        self.games_played += 1

    @classmethod
    def display_league_table(cls):
        sorted_teams = sorted(cls.teams, key=lambda team: team.points, reverse=True)
        for team in sorted_teams:
            print(f"{team.team_name:<15}{team.points:<10}{team.wins:<10}{team.losses:<10}{team.draws:<10}{team.games_played:<15}")


team1 = Team("Team A")
team2 = Team("Team B")
team3 = Team("Team C")

team1.update_stats("win")
team2.update_stats("loss")
team3.update_stats("draw")
team1.update_stats("win")
team2.update_stats("win")

Team.display_league_table()