# project/tests/test_ping.py


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200

    expected_response = {"environment": "dev", "ping": "pong", "testing": True}
    assert response.json() == expected_response
