""" Testing for Game class"""
import pytest
import os
import game
import shutil
import pdb
from typing import List

filepath = ".\\gametest\\"

@pytest.fixture
def setup_data():
    _game = game.Game(filepath)

    yield _game

    if os.path.exists(filepath):
        shutil.rmtree(filepath)

def test_creategame(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _game = setup_data
    _game.create_new_game()
    assert os.path.exists(filepath)
    assert os.path.exists(f'{filepath}turns')
    assert os.path.exists(f'{filepath}turns\\0')

def test_game_checkdict(setup_data):
    _game = setup_data
    _game.create_new_game()

    assert ( _game._options.get('humanplayers') is not None)
    assert ( _game._options.get('computerplayers') is not None)
    assert ( _game._options.get('startingmoney') is not None)
    assert ( _game._options.get('mapsize') is not None)
    assert ( _game._options.get('cityseparation') is not None)
    assert ( _game._options.get('sightingdistance') is not None)


def test_game_exists(setup_data):
    """ Checks to make sure game paths exists """
    _game = setup_data
    _game.create_new_game()
    assert setup_data.exists() == True

def test_game_exist_failed():
    _game = game.Game(filepath)
    assert _game.exists() == False

def test_game_count_players_no_players(setup_data):
    _game = setup_data
    _game.create_new_game()
    c = _game._players.count()

    assert(c==0)

def test_game_add_player(setup_data):
    _game = setup_data
    _game.create_new_game()

    _game._players.add("foo","test@test.com",_game._options.get('startingmoney'))

    assert (_game._players.count() == 1 )

    _game._players.load()
    assert (_game._players.count() == 1 )
    
    _game._players.clear()
    _game._players.load()
    assert (_game._players.count() == 1 )
    assert( _game._players._list[0].name == "foo")    
    assert (_game._players._list[0].money == _game._options.get('startingmoney'))

def test_game_add_player_from_dict(setup_data):
    _game = setup_data
    _game.create_new_game()

    d = {"id":0,"name":"foo","email":"test@test.com","money":_game._options.get('startingmoney'),"lastorders":[],"friends":[],"units":[],"removedunits":[]}

    _game._players.add_from_dict(d)

    assert (_game._players.count() == 1 )

    _game._players.load()
    assert (_game._players.count() == 1 )
    
    _game._players.clear()
    _game._players.load()
    assert (_game._players.count() == 1 )
    assert( _game._players._list[0].name == "foo")    
    assert (_game._players._list[0].money == _game._options.get('startingmoney'))

def test_game_find_player(setup_data):
    _game = setup_data
    _game.create_new_game()

    _game._players.add("foo","test1@test.com",44)
    _game._players.add("bar","tes2t@test.com",44)
    _game._players.add("one","test3@test.com",44)    
    assert (_game._players.count() == 3 )

    r=_game._players.find_by_id(1)
    assert ( r.name == "foo")

    r = _game._players.find_by_id(2)
    assert ( r.name == "bar")

    r = _game._players.find_by_id(3)
    assert ( r.name == "one")

    r = _game._players.find_by_id(3)
    assert ( r.email == "test3@test.com")

    r = _game._players.find_by_id(444)
    assert ( r==None)

def test_game_remove_by_id(setup_data):
    _game = setup_data
    _game.create_new_game()

    _game._players.add("foo","test1@test.com",0)
    _game._players.add("bar","tes2t@test.com",0)
    _game._players.add("one","test3@test.com",0)    
    _game._players.save()

    assert (_game._players.count() == 3 )

    r =_game._players.remove_by_id(2)
    assert (r == 2)
    assert (_game._players.count() == 2 )

    _game._players.save()
    _game._players.load()

    r = _game._players.find_by_id(3)
    assert ( r.email == "test3@test.com")

    r = _game._players.find_by_id(2)
    assert ( r==None)

    





