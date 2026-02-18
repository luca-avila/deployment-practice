import pytest


@pytest.mark.asyncio
async def test_get_counter_initial(client):
    """Test getting counter creates it with initial values."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 0
    assert data["times_clicked"] == 0


@pytest.mark.asyncio
async def test_increment(client):
    """Test incrementing the counter."""
    # First increment
    response = await client.post("/increment")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert data["times_clicked"] == 1
    
    # Second increment
    response = await client.post("/increment")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 2
    assert data["times_clicked"] == 2


@pytest.mark.asyncio
async def test_decrement(client):
    """Test decrementing the counter."""
    # First decrement (from 0)
    response = await client.post("/decrement")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == -1
    assert data["times_clicked"] == 1
    
    # Second decrement
    response = await client.post("/decrement")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == -2
    assert data["times_clicked"] == 2


@pytest.mark.asyncio
async def test_increment_and_decrement(client):
    """Test incrementing and decrementing together."""
    # Increment twice
    await client.post("/increment")
    await client.post("/increment")
    
    # Decrement once
    response = await client.post("/decrement")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert data["times_clicked"] == 3
    
    # Check final state
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert data["times_clicked"] == 3
