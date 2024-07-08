""" This is the Game Class """
import os
import json
from typing import List
import logging
import pdb

import player
import players

class Game:

    def __init__(self,folder=".\\game\\"):
        self.turn = 0
        self.slot = 0
        self.directory = folder
        self.players_file = f'{folder}players.json'
        #self._players = []
        self._players = players.Players(self.players_file)
        
        self.logger = logging.getLogger(__name__)
        self._players.read()
        
    def create_new_game(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self._players.read()
            

    def start_game(self):
        return
    
    def exists(self):
        return os.path.exists(self.directory)    
    
# region Players

    # def count_players(self):
    #     return len(self._players)

    # def read_players(self):
    #     if ( os.path.exists(self.players_file) == False):
    #         self._players = []
    #     else:
    #         with open(self.players_file, 'r') as file:
    #             data = json.load(file)
    #             self._players = []
    #             for item in data:
    #                 _p = player.Player(item['id'], item['name'], item['email'])
    #                 self._players.append(_p)

    # def add_player(self,name,email):
    #     self.read_players()
    #     id = self.count_players()
    #     id+=1
    #     self._players.append(player.Player(id,name,email))
        
    #     dict_list = [player.to_dict() for player in self._players]
    #     with open(self.players_file,'w') as file:
    #         json.dump(dict_list, file, indent=4)
        


# endregion
       	
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
    

      
