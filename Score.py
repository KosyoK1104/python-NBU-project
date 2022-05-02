import json
import os
from datetime import datetime
from pathlib import Path


class Score:
    FILE_NAME = '/score.json'
    DOCUMENTS_PATH = os.path.expanduser('~/Documents')
    DOCUMENTS_GAME_PATH = DOCUMENTS_PATH + '/PlayerVSAliens'

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.date = datetime.date(datetime.now())

    def data(self) -> dict:
        return {
            'name': self.name,
            'score': self.score,
            'date': self.date.strftime("%b %d, %Y")
        }

    def read(self) -> dict:
        if not os.path.exists(self.DOCUMENTS_GAME_PATH):
            os.mkdir(self.DOCUMENTS_GAME_PATH)

        f = Path(self.DOCUMENTS_GAME_PATH + self.FILE_NAME)
        f.touch(exist_ok=True)

        with open(f, "r") as file:
            # read the file
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {'players': []}

        return data

    def save(self):
        data = self.read()
        with open(self.DOCUMENTS_GAME_PATH + self.FILE_NAME, "w") as file:
            # add the new score
            data["players"].append(self.data())
            # write the file
            data['players'].sort(key=lambda x: x['score'], reverse=True)
            json.dump(data, file, indent=2)
