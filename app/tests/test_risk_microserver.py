#FastAPI
from fastapi import responses
from fastapi.testclient import TestClient

#Main APP
from app.main import app
from app.tests.mock_data import MockDataDb

client = TestClient(app)

fake_data_db = MockDataDb.get_query_data_metrics_log()
import pdb; pdb.set_trace()

def test__main():
    response = client.get("/")
    assert response.status_code == 200

def test_create_log():
    body ={
        "log_inf": "20140616 05:42:52 vm5 [4f8a7f94:533e226f] sshd transport algorithms: direction=client->server cipher=aes128-ctr mac=hmac-sha1 compression=none 10.10.10.1",
    }
    response = client.post("/log/", json=body)

    assert response.status_code == 200
    assert response.json()["ip_address"] == "10.10.10.1"
    assert response.json()["mac_address"] == "4f8a7f94:533e226f"

def test_get_metric():
    response = client.get("/metric/")

    assert response.status_code == 200



