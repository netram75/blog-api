from fastapi.testclient import TestClient
from main import app
# 1. Create the fake browser
client = TestClient(app)

# 2. Test getting all users
def test_get_all_users():
    response = client.get("/users")
    
    # Assert the status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the data returned is actually a list
    data = response.json()
    assert type(data) == list

def test_create_user():
    # 1. Send the POST request with perfectly matching data
    response = client.post(
        "/users",
        json={
            "id": 999, # Pydantic needs this, even though the server overwrites it
            "name": "Test Author", 
            "role": "Author",
            "email": "author@test.com"
        }
    )
    
    # 2. Assert the request was successful
    assert response.status_code == 200
    
    # 3. Assert the returned data matches what we expect
    data = response.json()
    assert data["name"] == "Test Author"
    assert data["email"] == "author@test.com"
    
    # 4. Ensure the fake database assigned them a REAL sequential ID (not 999!)
    assert data["id"] == 43