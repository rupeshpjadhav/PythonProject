import pytest

body = {
  "data": {
    "name": "Condenser Headphones",
    "price": 89.99,
    "category": "Electronics",
    "in_stock": True
  }
}


def test_post_newrecord(api):
    resp = api.post(body=body)
    api.print_json(resp)
    assert resp.status_code == 201


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
