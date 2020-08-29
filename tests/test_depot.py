from . import common
from app import depot
from app import __version__

from config import Config

import logging
import json
from typing import List


def test_main_procedure(client, auth_header, data):
    input_data: dict = {"stack_id": 1, "nodes": data}
    logging.debug(f"input data : {input_data}")

    logging.debug(f"endpoint: {common.ENDPOINT}")

    HEADERS: dict = dict(auth_header, **{"Content-Type": "application/json"})
    response = client.post(common.ENDPOINT, headers=HEADERS, json=input_data)
    output = json.loads(response.get_data())

    assert len(output) == 2
    assert all(ele in output["depots"][0] for ele in ["latitude", "longitude"])


def test_create_depot(df):
    lats: List[float] = df.latitude.tolist()
    lons: List[float] = df.longitude.tolist()

    assert depot.create_origin(lats, lons)
