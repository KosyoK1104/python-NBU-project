import pygame as pg
import json
import Game
from datetime import datetime


class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.date = datetime.date(datetime.now())

    def __str__(self) -> str:
        return f"{self.name} {self.score} {self.date}"

    def save(self):
        # handle the file in a way that it can be read and written
        with open("data/scores.json", "r+") as file:
            # read the file
            data = json.load(file)
            print(data)
            # add the new score
            data["players"].append(self.__str__())
            # write the file
            json.dump(data, file, indent=4)

