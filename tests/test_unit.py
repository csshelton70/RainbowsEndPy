import pytest
import os
from units import Units
from game import Game
import shutil
from typing import List

filepath = ".\\gametest\\"

@pytest.fixture
def setup_data():
    _game = Game(filepath)
    _game.Create_New_Game()
    _units = Units(filepath,10)

    yield _units

    if os.path.exists(filepath):
        shutil.rmtree(filepath)

def test_load(setup_data):
    """ Checks to make sure the gamefolder and player.txt file is created"""
    _unit = setup_data
    _unit.Load()

    assert(len(_unit._list) == 0)

    assert(os.path.exists(f'{filepath}units.json'))

def test_save(setup_data):
    _unit = setup_data
    _unit.Save()
    assert(os.path.exists(f'{filepath}units.json'))

def test_Add_Unit(setup_data):
    _unit = setup_data

    assert(_unit.Count() == 0)

    r = _unit.Who_Is_In_Hex(5)
    assert ( r == 0 )

    _unit.Add_Unit(1,1,5)
    _unit.Add_Unit(1,2,4)
    assert(_unit.Count() ==2)

    _unit.Add_Unit(1,2,4)
    _unit.Add_Unit(1,2,5)
    assert(_unit.Count() ==2)

    _unit.Add_Unit(1,2,6)
    assert(_unit.Count() ==3)

    r = _unit.Who_Is_In_Hex(5) 
    assert(r==1)

def test_Delete_All(setup_data):
    _unit = setup_data

    assert(_unit.Count() == 0)

    r = _unit.Who_Is_In_Hex(5)
    assert ( r == 0 )

    _unit.Add_Unit(1,1,5)
    _unit.Add_Unit(1,2,4)
    assert(_unit.Count() ==2)

    _unit.Delete_All()
    assert(_unit.Count() ==0)
