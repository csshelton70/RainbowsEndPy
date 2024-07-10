""" This is the Game Class """
import os
import json
from typing import List
import logging

from players import Players

class Game:
    _turn: int
    _slot: int
    _directory: str
    _players_file: str
    _players: Players
    _options : dict
       
    def __init__(self,folder=".\\game\\"):
        self._turn = 0
        self._slot = 0
        self._directory = folder
        self._options= dict(humanplayers=0, computerplayers=0, startingmoney=10,mapsize=35,cityseparation=3,sightingdistance=3)
        # // TODO: Write the options to the disk in the game folder so they can be modified by the user using text editor
        self._players = Players(f'{folder}players.json')
        
        self._logger = logging.getLogger(__name__)
        self._players.load()
        
    def create_new_game(self):
        if not os.path.exists(self._directory):
            self._logger.debug("    creating new game folder")
            os.makedirs(self._directory)
            os.makedirs(f'{self._directory}\\turns')
            os.makedirs(f'{self._directory}\\turns\\{self._turn}')
        self._players.load()
            

    def start_game(self):
        return
    
    def exists(self):
        return os.path.exists(self._directory)    
   


    #    # self.turn=0
    #    # players=players.Players()
    #    # players.init()

    # # initplayers(); - players.cc
    # # initmap(); - map.cc
    # # initunits(); - unit.cc

    # # writereports(); writerpt.cc
    # # save(); - save.cc

    # # redraw(); - windows.cc
    #     return
    
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
    

      
