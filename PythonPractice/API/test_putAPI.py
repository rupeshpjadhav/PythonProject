import pytest

body = {
  "data": {
    "name": "New Condenser Headphones",
    "price": 129.99,
    "category": "Electronics & Comm",
    "in_stock": True
  }
}


def test_updated_record(api, record_id):
    resp = api.put(record_id, body=body)
    print(f"\nRecord with {record_id} is updated")
    api.print_json(resp)
    assert resp.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
