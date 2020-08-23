from json import loads
from typing import List
from numpy import zeros

from flask import jsonify, make_response, request

from app import depot

from . import bp


@bp.route("/depot", methods=["POST"])
def depot_procedure():
    """
    Main RPC endpoint for passing input data for origin output.

    :latitude:      str of destination latitudes
    :longitude:     str of destination longitudes

    :return:        dict { "latitude": float, "longitude": float }        
    """
    body = loads(request.data)

    lats = zeros(len(body))
    lons = zeros(len(body))

    for i, row in enumerate(body):
        lats[i] = row["latitude"]
        lons[i] = row["longitude"]

    response = depot.create_origin(lats, lons)

    return jsonify(response)
