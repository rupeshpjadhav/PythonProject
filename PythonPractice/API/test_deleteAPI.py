import json
import requests
import pytest


def test_delete_singlerecord(base_url,headers,record_id,project_id):
    
    resp = requests.delete(f"{base_url}/{record_id}", params={"project-id":project_id}, headers=headers)
    print(f"\nRecord with {record_id} is deleted")
    assert resp.status_code == 204


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
