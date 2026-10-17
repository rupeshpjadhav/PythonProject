# PythonPractice/API/conftest.py
import os
from datetime import datetime

import pytest

from utils.api_client import APIClient


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(report_dir, exist_ok=True)
    config.option.htmlpath = f"{report_dir}/report_{now}.html"
    config.option.self_contained_html = True


@pytest.fixture(autouse=True)
def setup_teardown():
    print("Setting up ......")
    yield
    print("Tearing down")


@pytest.fixture(scope="session")
def api():
    return APIClient()


@pytest.fixture
def record_id(api):
    resp = api.get()
    return resp.json()["data"][0]["id"]  # returns first id
