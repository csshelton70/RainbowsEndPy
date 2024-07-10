import pytest

import map

@pytest.fixture
def setup_data():
    _map = map.Map()
    _map.CreateMap(10)

    yield _map


def test_create_map(setup_data):
    _map = setup_data

    assert(len(_map._hexes) == 100)
    assert(_map._hexes[0] == 0)
    assert(_map._hexes[99] == 0)

def test_is_on_map(setup_data):
    _map = setup_data

    assert(_map.is_on_map(0,0)==True)
    assert(_map.is_on_map(9,9)==True)
    assert(_map.is_on_map(10,9)==False)
    assert(_map.is_on_map(10,90)==False)

