""" """
import os
import json
from typing import List

import player

class Players:
    list = List

    def __init__(self,filename):
        self.list = []
        self.filename = filename

    def count(self):
        self.read()
        return len(self.list)
    
    def clear(self):
        self.list = []

    def read(self):
        if ( os.path.exists(self.filename) == False):
            self.list = []
        else:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.list = []
                for item in data:
                    _p = player.Player(item['id'], item['name'], item['email'])
                    self.list.append(_p)

    def add(self,name,email):
        self.read()
        id = self.count()
        id+=1
        self.list.append(player.Player(id,name,email))
        
        dict_list = [player.to_dict() for player in self.list]
        with open(self.filename,'w') as file:
            json.dump(dict_list, file, indent=4)
        