from fastapi import FastAPI

app = FastAPI()

products = []

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: dict):
    products.append(product)
    return product
