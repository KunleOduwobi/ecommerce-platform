import importlib

from fastapi.testclient import TestClient

#  This test assumes that the PostgreSQL container is running and accessible at the URL specified in the DATABASE_URL environment variable.
def test_create_product(postgres_container):
    # Import only after DATABASE_URL is set by the fixture
    import product_service.app.database as database
    import product_service.app.main as main

    importlib.reload(database)
    importlib.reload(main)

#   Create the database tables
    database.Base.metadata.create_all(bind=database.engine)

# 
    client = TestClient(main.app)

#   Create a new product
    response = client.post(
        "/products",
        json={"name": "Phone", "price": 800}
    )

#   Verify the response
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Phone"
    assert body["price"] == 800

#  Verify the product is in the database
    db = database.SessionLocal()
    try:
        product_in_db = db.query(main.Product).filter_by(name="Phone").first()
        assert product_in_db is not None
        assert product_in_db.price == 800
    finally:
        db.close()


