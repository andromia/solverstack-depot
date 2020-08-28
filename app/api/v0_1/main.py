from json import loads
from typing import List
from numpy import zeros
from flask import jsonify, make_response, request
import requests

from app import depot

from . import bp


CRUD_URL: str = "http://localhost:5006/api/v0.1/depot"


@bp.route("/depot", methods=["POST"])
def depot_procedure():
    """
    Main RPC endpoint for passing input data for origin output.

    :latitude:      str of destination latitudes
    :longitude:     str of destination longitudes

    :return:        dict { "latitude": float, "longitude": float }        
    """
    body = loads(request.data)
    stack_id = body["stack_id"]
    nodes = body["nodes"]

    lats = zeros(len(nodes))
    lons = zeros(len(nodes))

    for i, row in enumerate(nodes):
        lats[i] = row["latitude"]
        lons[i] = row["longitude"]

    results = depot.create_origin(lats, lons)

    try:
        response = requests.post(
            CRUD_URL,
            headers=request.headers,
            json={"stack_id": stack_id, "depots": [results]},
        )

        return make_response(jsonify(loads(response.text)), 200)

    except:

        return make_response(jsonify({"stack_id": stack_id, "depots": [results]}), 200)
