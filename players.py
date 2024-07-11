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

    def Count(self):
        self.Load()
        return len(self._list)
    
    def Clear(self):
        self._list = []

    def Load(self):
        if ( os.path.exists(self._filename) == False):
            self._list = []
        else:
            with open(self._filename, 'r') as file:
                data = json.load(file)
                self._list = []
                for item in data:
                    _p = Player()
                    _p.Populate_From_Dict(item)
                    self._list.append(_p)

    def Add(self,name,email, money):
        self.Load()
        id = self.Count()
        id+=1
        _p = Player()
        _p.Populate(id,name,email,money)
        self._list.append(_p)
        self.Save()

    def Add_From_Dict(self,d):
        self.Load()
        id = self.Count()
        id += 1
        d["id"] = id
        _p = Player()
        _p.Populate_From_Dict(d)
        self._list.append(_p)
        self.Save()
        
    def Save(self):
        dict_list = [player.To_Dict() for player in self._list]
        with open(self._filename,'w') as file:
            json.dump(dict_list, file, indent=4)

    def Find_By_Id(self,id):
#        player = next(filter(lambda player: player.id == id, self.list))
        f = (filter(lambda player: player.id == id, self._list))
        lst = list(f)
        ct = len(lst)
        if (ct > 0):
            return lst[0]
        else:
            return None

    def Remove_By_Id(self,id):
        if ( self.Find_By_Id(id) != None ):
            l= list(filter(lambda player: player.id != id, self._list))
            self._list = l
            self.Save()
            return len(self._list)

    
