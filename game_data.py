import os
import json

class GameData:
    # private
    _filename : str

    # public
    started : bool
    current_turn : int
    human_players : int
    computer_players : int
    starting_money : int
    map_size  : int
    city_separation : int
    sightdistance : int

    def __init__(self,filepath):
        self._filename = f'{filepath}gamedata.json'
        self.Load()

    def Initialize ( self ) -> None :
        self.human_players = 10
        self.computer_players = 0
        self.starting_money = 10
        self.map_size = 35
        self.city_separation = 3
        self.sight_distance = 3
        self.current_turn = 0
        self.started = False

    def Load(self):
        if ( os.path.exists(self._filename) == False):
            self.Initialize()
            self.Save()
        else:
            with open(self._filename, 'r') as file:
                data = json.load(file)
                self.current_turn = data["current_turn"]
                self.human_players = data["human_players"]
                self.computer_players = data["computer_players"]
                self.starting_money = data["starting_money"]
                self.map_size  = data["map_size"]
                self.city_separation = data["city_separation"]
                self.sight_distance = data["sight_distance"]
                self.started = data["started"]


    def Save(self):
        data = {"current_turn":self.current_turn, 
            "human_players":self.human_players,
            "computer_players":self.computer_players,
            "starting_money": self.starting_money,
            "map_size":self.map_size,
            "city_separation":self.city_separation,
            "sight_distance":self.sight_distance,
            "started":self.started}
        
        with open(self._filename,'w') as file:
            json.dump(data, file, indent=4)
    