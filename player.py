""" This is the Players Class """


class Player:
    id: int
    name: str
    email: str

    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "email": self.email
        }
    
    # def __repr__(self):
    #     return f"Playerid={self.id}, (name={self.name}, email={self.email})"




    # def count_players(self):
    #     json_object = self.read_players()
    #     if ( json_object == None):
    #         return 0
    #     else:
    #         return json_object

    # def read_players(self):
    #     if ( os.path.exists(self.directory)==False):
    #         return None
    #     else:
    #         with open(f'{self.directory}', 'r') as openfile:
    #             json_object = json.load(openfile)
    #             return json_object
            
    # def add_player(self):
    #     json_object = self.read_players(self.directory)
    #     with open(f'{self.directory}','a') as openfile:
    #         return
        

# static void countplayers()
# {
# 	file = fopen("players", "r");
# 	if (file == 0)
# 		error("Players file not found");

# 	humanplayers = 0;
# 	for (;;)
# 	{
# 		fgets(line, linesize, file);
# 		if (feof(file))
# 			break;
# 		parse();
# 		if (words[0][0])
# 			humanplayers++;
# 	}

# 	fclose(file);
# }
     #   return
    
 #   def read_players(self):
        # static void readplayers()
        # {
        # 	file = fopen("players", "r");
        # 	if (file == 0)
        # 		error("Unable to open players file");

        # 	int i = 0;
        # 	for (;;)
        # 	{
        # 		fgets(line, linesize, file);
        # 		if (feof(file))
        # 			break;
        # 		parse();
        # 		if (words[0][0] == 0)
        # 			continue;
        # 		player *p = players[i];

        # 		p->id = i + 1;
        # 		strcpy(p->name, "Player");
        # 		strcpy(p->email, words[0]);
        # 		p->money = startingmoney;
        # 		p->lastorders = 0;
        # 		i++;
        # 	}

        # 	fclose(file);
        # }
     #   return
    
 #   def initialize(self):
        # void initplayers()
        # {
        #     countplayers();
        #     playerscount = humanplayers + computerplayers;
        #     players = new player *[playerscount];
        #     players2 = new player *[playerscount];
        #     for (int i = 0; i < playerscount; i++)
        #         players[i] = new player;
        #     readplayers();
        # }
      #  return
    
  #  def find_player(self):
# player *findplayer(int id)
# {
# 	for (int i = 0; i < playerscount; i++)
# 	{
# 		player *p = players[i];
# 		if (p->id == id)
# 			return p;
# 	}
# 	return 0;
# }
    #    return
    
   # def remove_players(self):
            
    # void removeplayers()
    # {
    #     for (int i = 0; i < playerscount; i++)
    #     {
    #         player *p = players[i];
    #         if (p->units.count)
    #             continue;

    #         for (int j = 0; j < playerscount; j++)
    #             players[j]->friendly.remove(p);
    #         memmove(players + i, players + i + 1, (playerscount - i - 1) * sizeof(player *));
    #         playerscount--;
    #         i--;
    #     }
    # }
   #    return