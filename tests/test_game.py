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

    _game._players.add("foo","test@test.com")

    assert (_game._players.count() == 1 )
    _game._players.read()

    assert (_game._players.count() == 1 )
    
    _game._players.clear()
    _game._players.read()
    assert (_game._players.count() == 1 )
    assert( _game._players.list[0].name == "foo")    


