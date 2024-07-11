""" Testing for Game class"""
import pytest
import os
from game import Game
import shutil
from typing import List

filepath = ".\\gametest\\"

@pytest.fixture
def setup_data():
    _game = Game(filepath)

    yield _game

    if os.path.exists(filepath):
        shutil.rmtree(filepath)

def test_creategame(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _game = setup_data
    _game.Create_New_Game()
    assert os.path.exists(filepath)
    assert os.path.exists(f'{filepath}turns')
    assert os.path.exists(f'{filepath}turns\\0')

def test_game_checkdict(setup_data):
    _game = setup_data
    _game.Create_New_Game()

    assert ( _game._data.human_players is not None)
    assert ( _game._data.computer_players is not None)
    assert ( _game._data.starting_money is not None)
    assert ( _game._data.map_size is not None)
    assert ( _game._data.city_separation is not None)
    assert ( _game._data.sight_distance is not None)


def test_game_count_players_no_players(setup_data):
    _game = setup_data
    _game.Create_New_Game()
    c = _game._players.Count()

    assert(c==0)

def test_game_add_player(setup_data):
    _game = setup_data
    _game.Create_New_Game()

    _game._players.Add("foo","test@test.com",_game._data.starting_money)

    assert (_game._players.Count() == 1 )

    _game._players.Load()
    assert (_game._players.Count() == 1 )
    
    _game._players.Clear()
    _game._players.Load()
    assert (_game._players.Count() == 1 )
    assert( _game._players._list[0].name == "foo")    
    assert (_game._players._list[0].money == _game._data.starting_money)

def test_game_add_player_from_dict(setup_data):
    _game = setup_data
    _game.Create_New_Game()

    d = {"id":0,"name":"foo","email":"test@test.com","money":_game._data.starting_money,"lastorders":[],"friends":[],"units":[],"removedunits":[]}

    _game._players.Add_From_Dict(d)

    assert (_game._players.Count() == 1 )

    _game._players.Load()
    assert (_game._players.Count() == 1 )
    
    _game._players.Clear()
    _game._players.Load()
    assert (_game._players.Count() == 1 )
    assert( _game._players._list[0].name == "foo")    
    assert (_game._players._list[0].money == _game._data.starting_money)

def test_game_find_player(setup_data):
    _game = setup_data
    _game.Create_New_Game()

    _game._players.Add("foo","test1@test.com",44)
    _game._players.Add("bar","tes2t@test.com",44)
    _game._players.Add("one","test3@test.com",44)    
    assert (_game._players.Count() == 3 )

    r=_game._players.Find_By_Id(1)
    assert ( r.name == "foo")

    r = _game._players.Find_By_Id(2)
    assert ( r.name == "bar")

    r = _game._players.Find_By_Id(3)
    assert ( r.name == "one")

    r = _game._players.Find_By_Id(3)
    assert ( r.email == "test3@test.com")

    r = _game._players.Find_By_Id(444)
    assert ( r==None)

def test_game_remove_by_id(setup_data):
    _game = setup_data
    _game.Create_New_Game()

    _game._players.Add("foo","test1@test.com",0)
    _game._players.Add("bar","tes2t@test.com",0)
    _game._players.Add("one","test3@test.com",0)    
    _game._players.Save()

    assert (_game._players.Count() == 3 )

    r =_game._players.Remove_By_Id(2)
    assert (r == 2)
    assert (_game._players.Count() == 2 )

    _game._players.Save()
    _game._players.Load()

    r = _game._players.Find_By_Id(3)
    assert ( r.email == "test3@test.com")

    r = _game._players.Find_By_Id(2)
    assert ( r==None)

    





