""" """
import os
import json
from typing import List

from player import Player

class Players:
    # private
    _list : List
    _filename : str
    # public



    def __init__(self,filename):
        self._list = []
        self._filename = filename

    def count(self):
        self.load()
        return len(self._list)
    
    def clear(self):
        self._list = []

    def load(self):
        if ( os.path.exists(self._filename) == False):
            self._list = []
        else:
            with open(self._filename, 'r') as file:
                data = json.load(file)
                self._list = []
                for item in data:
                    _p = Player()
                    _p.populate_from_dict(item)
                    self._list.append(_p)

    def add(self,name,email, money):
        self.load()
        id = self.count()
        id+=1
        _p = Player()
        _p.populate(id,name,email,money)
        self._list.append(_p)
        self.save()

    def add_from_dict(self,d):
        self.load()
        id = self.count()
        id += 1
        d["id"] = id
        _p = Player()
        _p.populate_from_dict(d)
        self._list.append(_p)
        self.save()
        
    def save(self):
        dict_list = [player.to_dict() for player in self._list]
        with open(self._filename,'w') as file:
            json.dump(dict_list, file, indent=4)

    def find_by_id(self,id):
#        player = next(filter(lambda player: player.id == id, self.list))
        f = (filter(lambda player: player.id == id, self._list))
        lst = list(f)
        ct = len(lst)
        if (ct > 0):
            return lst[0]
        else:
            return None

    def remove_by_id(self,id):
        if ( self.find_by_id(id) != None ):
            l= list(filter(lambda player: player.id != id, self._list))
            self._list = l
            self.save()
            return len(self._list)

    
