"""
@author: Nathanael Jöhrmann
"""

# when distributing fixtures over several files, they can be added as plugin to conftest.py
# from glob import glob
#
#
# def refactor(string: str) -> str:
#     return string.replace("/", ".").replace("\\", ".").replace(".py", "")
#
#
# pytest_plugins = [
#     refactor(fixture) for fixture in glob("tests/fixtures/*.py") if "__" not in fixture
# ]
from pathlib import Path

import numpy as np
import pytest

from afm_tools.gdef_sticher import GDEFSticher
from gdef_reader.gdef_importer import GDEFImporter

AUTO_SHOW = False

@pytest.fixture(scope='session')
def gdf_example_01_path():
    yield Path.cwd().parent.joinpath("resources").joinpath("example_01.gdf")


@pytest.fixture(scope='session')
def gdef_importer(gdf_example_01_path):
    importer = GDEFImporter(gdf_example_01_path)
    yield importer


@pytest.fixture(scope='session')
def random_ndarray2d_data():
    # np.random.seed(1)
    rs = np.random.RandomState(np.random.MT19937(np.random.SeedSequence(1)))
    yield rs.random((256, 256)) * 1e-6 - 0.5e-6


@pytest.fixture(scope='session')
def gdef_measurement(gdef_importer):
    gdef_measurement = gdef_importer.export_measurements()[0]
    yield gdef_measurement


@pytest.fixture(scope='session')
def gdef_sticher(gdef_measurement):
    sticher = GDEFSticher([gdef_measurement, gdef_measurement])
    yield sticher


@pytest.fixture(scope="session", params=["GDEFMeasurement", "random_ndarray", "GDEFSticher"])
def data_test_cases(request, gdef_measurement, random_ndarray2d_data, gdef_sticher):
    case_dict = {
        "GDEFMeasurement": gdef_measurement,
        "random_ndarray": random_ndarray2d_data,
        "GDEFSticher": gdef_sticher
    }
    yield case_dict[request.param]


@pytest.fixture(scope='session')
def gdef_measurements(gdef_importer):
    gdef_measurements = gdef_importer.export_measurements()
    yield gdef_measurements