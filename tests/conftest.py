from app import create_app
from config import Config

import os
import logging
import pytest
from pandas import read_csv
from flask_jwt_extended import create_access_token


TEST_ROOT = os.path.dirname(os.path.abspath(__file__))
TEST_USER: dict = {"id": 1, "username": "test", "password": "password"}
CSV_TESTING_FILENAME = "destinations_testing_data.csv"
CSV_TESTING_FILEPATH = os.path.join(TEST_ROOT, CSV_TESTING_FILENAME)


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture()
def df():
    df = read_csv(CSV_TESTING_FILEPATH)
    logging.debug(f"filepath: {CSV_TESTING_FILEPATH} size: {df.shape}")

    return df


@pytest.fixture()
def data(df):
    DATA = [
        {"latitude": df.latitude.iloc[i], "longitude": df.longitude.iloc[i],}
        for i in range(len(df))
    ]

    return DATA


@pytest.fixture()
def client():
    yield create_app(TestConfig).test_client()


@pytest.fixture()
def auth_header():
    app = create_app(TestConfig)

    with app.app_context():
        token = create_access_token(TEST_USER)

    headers = {"Authorization": "Bearer {}".format(token)}

    return headers
