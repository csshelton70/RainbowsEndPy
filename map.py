    #-----------------------------------------------------------------------------------
	# A note on coordinate systems.
	# The game uses a total of four coordinate systems in different contexts.
	# These are:

	# H: A number from 0 to hexescount - 1.
	# Useful for iterating through all hexes
	# or referring to an arbitrary one irrespective of location.

	# X,Y: The usual Cartesian coordinates.

	# A,B: Axes inclined at 60 degrees rather than 90.
	# This system makes the distance formula simpler.

	# D: A direction from 0 to 5 counting clockwise from north.
    #-----------------------------------------------------------------------------------


from random import randint
from utilities import Is_Even, Is_Odd, Get_Sign

class Map:
    #private
    _terrain : dict
    _terrain_count: int
    _mapsize : 0
    _hexes : list[int]
    
    #public



    def __init__(self,folder=".\\game\\"):
        # terrain name = movement cost
        self._terrain = dict(water=0, plain=1, forest=2,mountain=3)
        self._terrain_count = len(self._terrain)

        return
    
    def Create_Map(self,mapsize) -> None:
        self._mapsize = mapsize
        hexcount = mapsize * mapsize

        self._hexes = []
        for i in range(hexcount):
            self._hexes.append(self._terrain['water'])

        i = randint(0,99) 
        self._hexes[i] = self._terrain['mountain']
        



# void initmap()
# {
# 	int *a = new int[hexescount];

# 	int n = hexescount / 2 - 1;
# 	for (int i = 0; i < n; i++)
# 	{
# 		int j = 0;
# 		for (int h = 0; h < hexescount; h++)
# 			if (offshore(h))
# 				a[j++] = h;
# 		h = a[random() % j];
# 		switch(random() % 4)
# 		{
# 		case 0:
# 			hexes[h].terrain = t_mountain;
# 			break;
# 		case 1:
# 			hexes[h].terrain = t_forest;
# 			break;
# 		default:
# 			hexes[h].terrain = t_plain;
# 		}
# 	}

# 	delete[] a;
# }
    def is_offshore(self,h) -> bool :
        if ( self._hexes[h] == self._terrain['water'] ):
            return 0
        
        for i in range(0,6):
            h2 = self._displace(h,i)
            if (( h2 >= 0 ) and (self._hexes[h2]==0)):
                return 1
            
        return 0

        
# static int offshore(int h)
# {
# 	if (hexes[h].terrain)
# 		return 0;
# 	for (int d = 0; d < 6; d++)
# 	{
# 		int h2 = displace(h, d);
# 		if (h2 >= 0 && hexes[h2].terrain)
# 			return 1;
# 	}
# 	return 0;
# }

# int findterrain(char *s)
# {
# 	for (int i = 0; i < terrainscount; i++)
# 		if (!stricmp(terrains[i].name, s))
# 			return i;
# 	return -1;
# }

# int findhex(char *s)
# {
# 	int x = atoi(s);
# 	char *s2 = strchr(s, '/');
# 	if (!s2)
# 		s2 = strchr(s, ',');
# 	if (!s2)
# 		return -1;
# 	int y = atoi(s2 + 1);
# 	if (!onmap(x, y))
# 		return -1;
# 	return xytoh(x, y);
# }

# char *idstr(int h)
# {
# 	static char s[40];
# 	int x = htox(h);
# 	int y = htoy(h);
# 	sprintf(s, "[%d/%d]", x, y);
# 	return s;
# }

# char *nameid(int h)
# {
# 	static char s[wordsize + 20];
# 	terrain *t = &terrains[hexes[h].terrain];
# 	int x = htox(h);
# 	int y = htoy(h);
# 	sprintf(s, "%s [%d/%d]", t->name, x, y);
# 	s[0] = toupper(s[0]);
# 	return s;
# }

    def is_on_map(self,x,y) -> bool:
        return ((x >= 0 ) and ( x< self._mapsize) and ( y >=0 ) and (y < self._mapsize))
    
    def xy_to_h(self,x,y) -> int:
        return y * self._mapsize + x

    def h_to_x(self,h) -> int:
        return h % self._mapsize

    def h_to_y(self,h) -> int:
        return int(h / self._mapsize)

    def displace(self,h,d) -> int:
        x = self.h_to_x(h)
        y = self.h_to_y(h)

        if (d == 0):
            y-=1
        elif (d ==1 ):
            if (Is_Even(x)):
                y-=1
            x+=1
        elif ( d==2):
            if ( Is_Odd(x)):
                y+=1
            x+=1
        elif (d==3):
            y+=1
        elif (d==4):
            if (Is_Odd(x)):
                y+=1
            x-=1
        elif (d==5):
            if (Is_Even(x)):
                y-=1
            x-=1

        if (self.is_on_map(x,y)):
            return -1
        
        return self.xy_to_h(x,y)

    def h_to_a(self,h) -> int:
        x = self.h_to_x(h)
        y = self.h_to_y(h)

        return int((x+1)/2+y)

    def h_to_b(self,h) -> int:
        x = self.h_to_x(h)
        y = self.h_to_y(h)

        return int((x/2)-y)

    def distance(self,h1,h2) -> int:
        a1 = self.h_to_a(h1)
        b1 = self.h_to_b(h1)

        a2 = self.h_to_a(h2)
        b2 = self.h_to_b(h2)

        da = a1-a2
        db = b1-b2

        s = bool(Get_Sign(da) == Get_Sign(db))

        da = abs(da)
        db = abs(db)

        if (s):
            return da+db
        else:
            return max(da,db)


# void event(int h, char *s)
# {
# 	static char buf[linesize];
# 	sprintf(buf, "%d: %s.", slot, s);
# 	hexevent *he = new hexevent;
# 	he->event = copy(buf);
# 	for (int i = 0; i < playerscount; i++)
# 		if (cansee(players[i], h))
# 			he->players.add(players[i]);
# 	hexes[h].events.add(he);
# }

# void event(int h, char *s, char *s2)
# {
# 	sprintf(buf, "%s %s", s, s2);
# 	event(h, buf);
# }

# void event(int h, char *s, char *s2, char *s3)
# {
# 	sprintf(buf, "%s %s %s", s, s2, s3);
# 	event(h, buf);
# }

# void event(int h, char *s, char *s2, char *s3, char *s4)
# {
# 	sprintf(buf, "%s %s %s %s", s, s2, s3, s4);
# 	event(h, buf);
# }

# void event(int h, char *s, char *s2, char *s3, char *s4, char *s5)
# {
# 	sprintf(buf, "%s %s %s %s %s", s, s2, s3, s4, s5);
# 	event(h, buf);
# }
