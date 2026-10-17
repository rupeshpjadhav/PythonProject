import json
import requests
import pytest


body = {
  "data": {
    "name": "New Condenser Headphones",
    "price": 129.99,
    "category": "Electronics & Comm",
    "in_stock": True
  }
}

def test_updated_record(base_url,project_id,headers,record_id):
    resp = requests.put(f"{base_url}/{record_id}", params={"project_id":project_id}, json=body, headers=headers)
    print(resp.status_code)
    print(f"\n Record with {record_id} is updated")
    print(json.dumps(resp.json(), indent=4))
    assert resp.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
