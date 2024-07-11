import pytest
from player import Player
from typing import List

def test_player_creation():
    id = 1
    name="foo"
    email="a@a.com"
    _player = Player()
    _player.Populate(id,name,email,44)

    assert ( id == _player.id)
    assert ( name == _player.name)
    assert ( email == _player.email)
    assert ( _player.money == 44 )


def test_player_list_creation():
    _players = []
    _players.clear
    
    id = 1
    name="foo"
    email="a@a.com"
    _p = Player()
    _p.Populate(id,name,email,35)
    _players.append(_p)

    id = 2
    name="boo"
    email="2@2.com"
    _p2 = Player()
    _p2.Populate(id,name,email,35)
    _players.append(_p2)

    print (_players[0])

    assert ( len(_players) == 2 )
    assert ( _players[0].id == 1)
    assert ( _players[1].id == 2)
    assert ( _players[0] != _players[1])
    assert ( _players[0].money == _players[1].money)



