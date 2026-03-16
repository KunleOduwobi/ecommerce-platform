import httpx
import psycopg2

BASE_URL = "http://127.0.0.1:8000"


def test_create_product():
    response = httpx.post(
        f"{BASE_URL}/products",
        json={"name": "Tablet", "price": 500}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Tablet"

    conn = psycopg2.connect(
        dbname="ecommerce",
        user="ecommerce_user",
        password="mypassword123",
        host="localhost"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM products WHERE name='Phone'"
    )

    result = cursor.fetchone()

    assert result[0] == "Phone"

    conn.close()



# def test_get_products():
#     response = httpx.get(f"{BASE_URL}/products")

#     assert response.status_code == 200
