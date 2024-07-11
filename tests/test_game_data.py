""" Testing for Game class"""
import pytest
import os
from game_data import GameData
import shutil
import pdb
from typing import List

filepath = ".\\gametest\\"

@pytest.fixture
def setup_data():
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    d = None

    yield d 

    if os.path.exists(filepath):
        shutil.rmtree(filepath)

def test_load_data_no_file(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _gd = GameData(filepath)

    assert os.path.exists(filepath)
    assert ( _gd.current_turn == 0)

def test_save_data_no_file(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _gd = GameData(filepath)

    assert os.path.exists(filepath)
    assert ( _gd.current_turn == 0)

    _gd.current_turn = 999
    assert ( _gd.current_turn == 999)

    _gd.Load()

    assert(_gd.current_turn == 0)

def test_double_loAD(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _gd = GameData(filepath)
    _gd.Load()
    _gd.Load()

    assert(_gd.human_players == 10)

    _gd.human_players = 11
    _gd.Save()
    _gd.Load()

    assert(_gd.human_players == 11)

