from . import bp
from app import depot
from json import loads
from typing import List
from numpy import zeros
from flask import jsonify, make_response, request
import requests


CRUD_URL: str = "http://localhost:5006/api/v0.1/depot"


@bp.route("/depot", methods=["POST"])
def depot_procedure():
    """
    Main RPC endpoint for passing input data for origin output.

    :latitude:      str of destination latitudes
    :longitude:     str of destination longitudes
    """
    body: dict = loads(request.data)
    stack_id: int = body["stack_id"]
    nodes: list = body["nodes"]

    lats: list = zeros(len(nodes))
    lons: list = zeros(len(nodes))

    for i, row in enumerate(nodes):
        lats[i]: float = row["latitude"]
        lons[i]: float = row["longitude"]

    results: dict = depot.create_origin(lats, lons)

    try:
        response = requests.post(
            CRUD_URL,
            headers=request.headers,
            json={"stack_id": stack_id, "depots": [results]},
        )

        return make_response(jsonify(loads(response.text)), 200)

    except:

        return make_response(jsonify({"stack_id": stack_id, "depots": [results]}), 200)
