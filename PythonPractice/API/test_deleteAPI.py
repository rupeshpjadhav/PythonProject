import pytest


def test_delete_singlerecord(api, record_id):
    resp = api.delete(record_id)
    print(f"\nRecord with {record_id} is deleted")
    assert resp.status_code == 204


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
