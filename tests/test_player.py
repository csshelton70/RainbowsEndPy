import pytest
import player
from typing import List

def test_player_creation():
    id = 1
    name="foo"
    email="a@a.com"
    _player = player.Player(id,name,email)

    assert ( id == _player.id)
    assert (name == _player.name)
    assert (email == _player.email)

def test_player_list_creation():
    _players = []
    _players.clear
    
    id = 1
    name="foo"
    email="a@a.com"
    _p = player.Player(id,name,email)
    _players.append(_p)

    id = 2
    name="boo"
    email="2@2.com"
    _p2 = player.Player(id,name,email)
    _players.append(_p2)


    assert ( len(_players) == 2 )
    assert ( _players[0].id == 1)
    assert ( _players[1].id == 2)
    assert ( _players[0] != _players[1])



# def test_players_count_0_players(setup_data):
#     _players = players.Players(setup_data.directory)
#     ct = _players.count_players()
#     assert ct == 0

# def test_players_count_players(setup_data):
#     _players = players.Players(setup_data.directory)
#     ct = _players.count_players()
#     assert ct == 0    

