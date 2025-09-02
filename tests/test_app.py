from app import app

def test_home():
    with app.test_client() as c:
        resp = c.get("/")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["message"] == "Hello CI/CD!"
