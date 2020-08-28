from . import common
from app import create_app, depot
from app import __version__

from config import Config

import logging
import pytest
import json


def test_main_procedure(client, auth_header, data):
    input_data = data
    logging.debug(f"input data : {input_data}")

    endpoint = f"/api/{__version__}/depot"
    logging.debug(f"endpoint: {endpoint}")

    HEADERS: dict = dict(auth_header, **{"Content-Type": "application/json"})
    response = client.post(
        endpoint, headers=HEADERS, json={"stack_id": 1, "nodes": input_data}
    )
    output = json.loads(response.get_data())

    assert len(output) == 2
    assert all(ele in output["depots"][0] for ele in ["latitude", "longitude"])


def test_create_depot(df):
    lats = df.latitude.tolist()
    lons = df.longitude.tolist()

    assert depot.create_origin(lats, lons)
