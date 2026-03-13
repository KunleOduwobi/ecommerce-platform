import httpx

BASE_URL = "http://127.0.0.1:8000"


def test_create_product():
    response = httpx.post(
        f"{BASE_URL}/products",
        json={"name": "Laptop", "price": 1000}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_get_products():
    response = httpx.get(f"{BASE_URL}/products")

    assert response.status_code == 200
