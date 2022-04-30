import pygame as pg
import json
import Game
from datetime import datetime


class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.date = datetime.date(datetime.now())

    def __str__(self):
        return self.name + " " + str(self.score) + " " + str(self.date)

    def write(self):
        # this DOESN'T WORK BECAUSE OF SELF.NAME
        new_score = {"name": self.name, "score": int(self.score), "date": str(self.date)}
        json_string = json.dumps(new_score)
        json_file = open("data/scores.json", "w")
        json_file.write(json_string)
        json_file.close()

