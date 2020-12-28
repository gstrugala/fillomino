import pytest
from pandas import read_pickle
from pandas.testing import assert_frame_equal
from pkg_resources import resource_filename

from fillomino.buildpermap import build_cooling_permap, build_heating_permap


@pytest.fixture
def manufacturer_table(mode):
    return read_pickle(f"data/manufacturer-table-{mode}.pkl")


@pytest.fixture
def manufacturer_data_file(mode):
    path = f"resources/manufacturer-data-{mode}.txt"
    return resource_filename('fillomino', path)


@pytest.mark.parametrize('mode', ['heating', 'cooling'])
def test_build_permap(mode, manufacturer_table, manufacturer_data_file):
    build_permap = {'cooling': build_cooling_permap,
                    'heating': build_heating_permap}[mode]
    table = build_permap(manufacturer_data_file)
    assert_frame_equal(table, manufacturer_table)
