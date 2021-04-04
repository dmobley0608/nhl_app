from bs4 import BeautifulSoup
import requests


class AutoDataRetrieval:
    def __init__(self):
        self.url = 'https://www.espn.com/nhl/standings/_/group/league'
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.tables = soup.find_all(class_='hide-mobile')
        self.stats = soup.find_all(class_='stat-cell')
        self.teams = []
        self.team_points = []

    def get_team_order(self):
        teams = self.tables
        count = 1
        for team in teams:
            self.teams.append(team.text)
            count += 1
        return self.teams

    def get_points(self):
        # get all the stats
        count = 1
        stats = []
        # narrow stats
        for score in self.stats:
            if count % 5 == 0:
                stats.append(score.text)
            count += 1
        # find team league points
        i = 0
        for stat in stats:
            if i % 3 == 0:
                self.team_points.append(stat)
            i += 1

        return self.team_points

    def get_wins(self):
        wins = []
        count = 1
        for stat in self.stats:
            if count < len(self.stats):
                wins.append(self.stats[count].text)
                count += 15
        return wins

    def get_loses(self):
        loses = []
        count = 2
        for stat in self.stats:
            if count < len(self.stats):
                loses.append(self.stats[count].text)
                count += 15
        return loses
