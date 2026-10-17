# PythonPractice/API/conftest.py
import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api/collections/products/records")
PROJECT_ID = os.getenv("PROJECT_ID", "50550")


@pytest.fixture
def headers():
    api_key = os.getenv("MY_API_KEY")
    assert api_key, "MY_API_KEY is missing - add it to .env"
    return {"x-api-key": api_key, "Accept": "application/json"}

@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def project_id():
    return PROJECT_ID

@pytest.fixture
def record_id(base_url,headers, project_id):
    resp = requests.get(base_url,params={"project_id":project_id}, headers=headers)
    return resp.json()["data"][0]["id"] # returns first id