import json
import requests
import pytest


def test_get_allrecords(base_url,project_id,headers):
    resp = requests.get(base_url, params={"project_id":project_id}, headers=headers)
    print(resp.status_code)
    print(json.dumps(resp.json(), indent=4))
    assert resp.status_code == 200


def test_get_singlerecord(base_url,project_id,headers,record_id):
    resp = requests.get(f"{base_url}/{record_id}",params={"project_id":project_id}, headers=headers)
    print(json.dumps(resp.json(), indent=4))
    assert resp.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
