import os
import json

class GameData:
    # private
    _filename : str

    # public
    current_turn : int

    def __init__(self,filepath):
        self._filename = f'{filepath}gamedata.json'
        self.load()

    def load(self):
        if ( os.path.exists(self._filename) == False):
            self.current_turn = 0
            self.save()
        else:
            with open(self._filename, 'r') as file:
                data = json.load(file)
                self.current_turn = data["current_turn"]

                # for item in data:
                #     _p = Player()
                #     _p.populate_from_dict(item)
                #     self.list.append(_p)
    
    def save(self):
        data = {"current_turn":self.current_turn}
        with open(self._filename,'w') as file:
            json.dump(data, file, indent=4)
    