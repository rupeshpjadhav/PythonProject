import pytest


def test_get_allrecords(api):
    resp = api.get()
    api.print_json(resp)
    assert resp.status_code == 200


def test_get_singlerecord(api, record_id):
    resp = api.get(record_id)
    api.print_json(resp)
    assert resp.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
