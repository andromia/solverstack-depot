from . import common
from app import origin


def test_geocode():
    lats = common.TESTING_CSV_DF.latitude.tolist()
    lons = common.TESTING_CSV_DF.longitude.tolist()

    assert origin.create_origin(lats, lons)