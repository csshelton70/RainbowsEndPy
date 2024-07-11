import os
import json
from dataclasses import dataclass

@dataclass
class Unit:
    player_id: int
    type_id: int
    h: int


class Units():
    # private
    _types = dict[dict]
    _list = []
    _filename = str
    _max_players:int
    # public

    def __init__(self, filepath, max_players):
        self._types = { "1":{"name":"city",     "build_cost":20,"upkeep_cost":-10,"movement":0,"attack":0,"defense":0,"range":0},
                        "2":{"name":"settlers", "build_cost":10,"upkeep_cost":1,"movement":3,"attack":0,"defense":2,"range":0},
                        "3":{"name":"infantry", "build_cost":10,"upkeep_cost":1,"movement":3,"attack":4,"defense":4,"range":0},
                        "4":{"name":"tanks",    "build_cost":20,"upkeep_cost":2,"movement":6,"attack":8,"defense":6,"range":0},
                        "5":{"name":"artillery","build_cost":20,"upkeep_cost":2,"movement":3,"attack":1,"defense":4,"range":2}} 
        self._list = []
        self._filename = f'{filepath}units.json'
        self._max_players = max_players
        return

    def Load(self):
        if ( os.path.exists(self._filename) == False):
            self._list = []
            self.Save()
        else:
            with open(self._filename, 'r') as file:
                data = json.load(file)
                self._list = []
                for item in data:
                    _u = Unit(item["player_id"], item["type_id"],item["h"])
                    self._list.append(_u)
    
    def Save(self):
        dict_list = [u.To_Dict() for u in self._list]
        with open(self._filename,'w') as file:
            json.dump(dict_list, file, indent=4)

# array units;
    def Delete_All(self):
        self._list = []
        return

    def Count(self) -> int:
        return len(self._list)

    def Init_Cities(self) -> bool:
        return True
# static int initcities()
# {
# 	// Create one city per player

# 	int i;
# 	for (i = 0; i < playerscount; i++)
# 	{
# 		unit *c = new unit;
# 		c->id = 1;
# 		strcpy(c->name, "City");
# 		c->type = u_city;
# 		c->player = players[i];
# 		do
# 			c->hex = random() % hexescount;
# 		while (!hexes[c->hex].terrain);
# 		addunit(c);
# 	}

# 	// Separate them as far as possible

# 	int more;
# 	do
# 	{
# 		more = 0;
# 		for (i = 0; i < playerscount; i++)
# 		{
# 			unit *c = (unit *)units[i];
# 			int r = nearestcity(c->hex, c);
# 			int a[6];
# 			int j = 0;
# 			for (int d = 0; d < 6; d++)
# 			{
# 				int h = displace(c->hex, d);
# 				if (h < 0)
# 					continue;
# 				if (!hexes[h].terrain)
# 					continue;

# 				if (nearestcity(h, c) > r)
# 					a[j++] = h;
# 			}
# 			if (j == 0)
# 				continue;

# 			moveunit(c, a[random() % j]);
# 			more = 1;
# 		}
# 	}
# 	while (more);

# 	// Check if they're now adequately separated
# 	for (i = 0; i < playerscount; i++)
# 	{
# 		unit *c = (unit *)units[i];
# 		if (nearestcity(c->hex, c) < cityseparation)
# 		{
# 			deletecities();
# 			return 0;
# 		}
# 	}
# 	return 1;
# }
    def Init_Units(self) -> bool:
        for i in range(1,self._max_players):
            if ( self.Init_Cities()):
                return True
        return False

    def Add_Unit(self,player_id,type_id,h):
        if ( self.Who_Is_In_Hex(h) == 0 ):
            _u = Unit(player_id, type_id, h)
            self._list.append(_u)

        return

    def Who_Is_In_Hex(self,h) -> int:
        if ( len(self._list) == 0):
            return 0

        r = [unit for unit in self._list if unit.h == h ]

        if (len(r) > 0):
           return r[0].player_id
        else:
            return 0
        


# void addunit(unit *u)
# {
# 	units.add(u);
# 	hexes[u->hex].units.add(u);

# 	player *p = u->player;
# 	if (!p->units.count)
# 	{
# 		p->units.add(u);
# 		return;
# 	}
# 	unit *u2 = (unit *)p->units[p->units.count - 1];
# 	if (u2->id < u->id)
# 	{
# 		p->units.add(u);
# 		return;
# 	}
# 	for (int i = 0;; i++)
# 	{
# 		u2 = (unit *)p->units[i];
# 		if (u2->id > u->id)
# 		{
# 			p->units.insert(i, u);
# 			return;
# 		}
# 	}
# }


    def Find_By1_Id(self):
        return
# int findunittype(char *s)
# {
# 	if (strlen(s) < 3)
# 		return -1;
# 	for (int i = 0; i < sizeof unittypes / sizeof(char *); i++)
# 		if (!memicmp(s, unittypes[i].name, 3))
# 			return i;
# 	return -1;
# }
    def Find_By_Player_and_Id(self,playerId, unitId):
        return
# unit *findunit(player *p, int id)
# {
# 	for (int i = 0; i < p->units.count; i++)
# 	{
# 		unit *u = (unit *)p->units[i];
# 		if (u->id == id)
# 			return u;
# 	}
# 	return 0;
# }

    
# char *pid(unit *u)
# {
# 	static char s[40];
# 	sprintf(s, "[%d-%d]", u->player->id, u->id);
# 	return s;
# }

# char *namepid(unit *u)
# {
# 	static char s[wordsize + 40];
# 	sprintf(s, "%s [%d-%d]", u->name, u->player->id, u->id);
# 	return s;
# }

# char *namepidtype(unit *u)
# {
# 	static char s[wordsize + 100];
# 	char *type = unittypes[u->type].name;
# 	sprintf(s, "%s [%d-%d] (%s)", u->name, u->player->id, u->id, type);
# 	return s;
# }
    def Nearest_City(g, id ):
        return
# int nearestcity(int h, unit *c)
# {
# 	int r = INT_MAX;
# 	for (int i = 0; i < units.count; i++)
# 	{
# 		unit *c2 = (unit *)units[i];
# 		if (c2->type != u_city)
# 			continue;
# 		if (c2 == c)
# 			continue;

# 		int r2 = distance(h, c2->hex);
# 		r = min(r, r2);
# 	}
# 	return r;
# }

    def Move_Unit(unit,h):
        return
# void moveunit(unit *u, int h)
# {
# 	hexes[u->hex].units.remove(u);
# 	u->hex = h;
# 	hexes[h].units.add(u);
# }

    def Remove_Unit(id):
        return
# void removeunit(unit *u)
# {
# 	units.remove(u);
# 	u->player->units.remove(u);
# 	u->player->removedunits.add(u);
# 	hexes[u->hex].units.remove(u);
# 	u->removed = 1;
# }
