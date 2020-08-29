from app import create_app
from config import Config

import os
import logging
import pytest
from pandas import DataFrame, read_csv
from flask_jwt_extended import create_access_token


TEST_ROOT: str = os.path.dirname(os.path.abspath(__file__))
TEST_USER: dict = {"id": 1, "username": "test", "password": "password"}
CSV_TESTING_FILENAME: str = "destinations_testing_data.csv"
CSV_TESTING_FILEPATH: str = os.path.join(TEST_ROOT, CSV_TESTING_FILENAME)


class TestConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite://"


@pytest.fixture()
def client():
    yield create_app(TestConfig).test_client()


@pytest.fixture()
def auth_header():
    app = create_app(TestConfig)

    with app.app_context():
        token: str = create_access_token(TEST_USER)

    headers: dict = {"Authorization": "Bearer {}".format(token)}

    return headers


@pytest.fixture()
def df():
    df: DataFrame = read_csv(CSV_TESTING_FILEPATH)
    logging.debug(f"filepath: {CSV_TESTING_FILEPATH} size: {df.shape}")

    return df


@pytest.fixture()
def data(df):
    DATA: list = [
        {"latitude": df.latitude.iloc[i], "longitude": df.longitude.iloc[i],}
        for i in range(len(df))
    ]

    return DATA
