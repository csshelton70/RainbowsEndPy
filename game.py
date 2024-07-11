""" This is the Game Class """
import os
import json
from typing import List
import logging
import inspect

from players import Players
from game_data import GameData

class Game:
    #private
    _directory: str
    _players_file: str
    _players: Players
    _data : GameData
    _logger : logging.Logger
    _units : dict[dict]
    #public

#   Initializes the game object       
    def __init__(self,folder=".\\game\\"):
        self._directory = folder
        self._logger = logging.getLogger(__name__)
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")

#   Used to create a new game.  
#       Creates folder structure
#       Creates gamedata file
#       Creates player file        
    def Create_New_Game(self):
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")

        if not os.path.exists(self._directory):
            os.makedirs(self._directory)
            os.makedirs(f'{self._directory}\\turns')
            os.makedirs(f'{self._directory}\\turns\\0')
        
        self._data = GameData(self._directory)

        self._players = Players(f'{self._directory}players.json')
        self._players.Load()

        self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=New game created")            
    # # initmap(); - map.cc
    # # initunits(); - unit.cc

    # # writereports(); writerpt.cc
    # # save(); - save.cc

    # # redraw(); - windows.cc
    #     return

    # Adds a player to the game data file
    #   This can only be done before the game starts.
    def Add_Player(self,name:str, email:str) -> None:
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}{name}{email}")
        r = self._players.Add(name, email, self._data.starting_money)
        self._logger.debug(f"       {inspect.currentframe().f_code.co_name} Result=Playerid={r}")

    def Clear_Players(self)-> None:
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        self._players.Clear()

    def Load_Players(self)->None:
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        self._players.Load()

    def Start_Game(self) -> None:
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        self._data.started = True
        self._data.Save()
        self.Run_Turn()



    # def player_orders():
    # #     	for (slot = 1; slot <= maxorders; slot++)
    # # {
    # # 	int si = slot - 1;
    # # 	for (int i = 0; i < playerscount; i++)
    # # 	{
    # # 		player *p = players[i];
    # # 		if (si >= p->orders.count)
    # # 			continue;
    # # 		order *o = (order *)p->orders[si];
    # # 		doorder(p, o);
    # # 	}
    # # }
    #     return
    
    # def unit_orders(phase):
    # # int unitscount = units.count;
    # # unit **units2 = new unit *[unitscount];
    # # memcpy(units2, units.data, unitscount * sizeof(unit *));
    # # shuffle(units2, unitscount);

    # # int si = slot - 1;
    # # for (int i = 0; i < unitscount; i++)
    # # {
    # # 	unit *u = units2[i];
    # # 	if (u->removed)
    # # 		continue;
    # # 	if (si >= u->orders.count)
    # # 		continue;
    # # 	order *o = (order *)u->orders[si];

    # # 	switch (o->type)
    # # 	{
    # # 	case o_build:
    # # 	case o_drop:
    # # 		if (phase != 2)
    # # 			continue;
    # # 		break;
    # # 	case o_move:
    # # 		if (phase != 1)
    # # 			continue;
    # # 		break;
    # # 	default:
    # # 		if (phase)
    # # 			continue;
    # # 	}
    # # 	doorder(u, o);
    # # }

    # # delete[] units2;        
    #     return
    
    # def unit_orders():
    # #     	for (slot = 1; slot <= maxorders; slot++)
    # # {
    # # 	unitorders(0);
    # # 	unitorders(1);
    # # 	combat(); - rules.cc
    # # 	capture(); - rules.cc
    # # 	unitorders(2); - game.cc
    # # }
    #     return
    def Run_Turn(self):
        self._logger.debug(f"     {__name__}:{inspect.currentframe().f_code.co_name}")
        return
    # def run_turn():
    # # slot = 0;
    # # load(); - save.cc
    # # readorders() - order.cc
    # # decideorders(); - ai.cc
    # # adjustorders(); - order.cc

    # # turn++;
    # # refreshunits(); - rules.cc
    # # playerorders(); - game.cc
    # # unitorders(); - game.cc
    # # income(); - rules.cc
    # # upkeep(); - rules.cc

    # # writereports(); - writerpt.cc
    # # removeplayers(); - player.cc
    # # save(); - save.cc

    # # redraw();
    #     return
    

      
