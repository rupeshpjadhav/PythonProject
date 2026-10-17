import json
import requests
import pytest

body = {
  "data": {
    "name": "Condenser Headphones",
    "price": 89.99,
    "category": "Electronics",
    "in_stock": True
  }
}

def test_post_newrecord(base_url,project_id,headers):
    resp = requests.post(base_url,params={"project_id":project_id}, json=body, headers=headers)
    print(resp.status_code)
    print(json.dumps(resp.json(), indent=4))
    assert resp.status_code == 201



if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
