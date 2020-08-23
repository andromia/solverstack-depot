from . import common
from app import create_app, depot
from app import __version__

from config import Config

import logging
import pytest
import json


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture
def client():
    yield create_app(TestConfig).test_client()


def test_main_procedure(client):
    input_data = common.DATA
    logging.debug(f"input data : {input_data}")

    endpoint = f"/api/{__version__}/depot"
    logging.debug(f"endpoint: {endpoint}")

    response = client.post(endpoint, json=input_data)
    output = json.loads(response.get_data())

    assert len(output) == 2
    assert all(ele in ["latitude", "longitude"] for ele in output)


def test_create_depot():
    lats = common.TESTING_CSV_DF.latitude.tolist()
    lons = common.TESTING_CSV_DF.longitude.tolist()

    assert depot.create_origin(lats, lons)
