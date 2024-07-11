import os
import json
import logging
import inspect

class GameData:
    # private
    _filename : str
    _logger : logging.Logger

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
        self._logger = logging.getLogger(__name__)
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        self._filename = f'{filepath}gamedata.json'
        self.Load()

    def InitializeDefaultData ( self ) -> None :
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        self.human_players = 10
        self.computer_players = 0
        self.starting_money = 10
        self.map_size = 35
        self.city_separation = 3
        self.sight_distance = 3
        self.current_turn = 0
        self.started = False
        self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=Initialized")

    def Load(self) -> None:
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")

        if ( os.path.exists(self._filename) == False):
            self.InitializeDefaultData()
            self.Save()
            self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=Created new file")
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
            self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=Loaded existing file")


    def Save(self):
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")

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

        self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=Saved to file")

    