from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Product


app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# API now uses the DB session for data storage and retrieval
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints now interact with the database
@app.post("/products")
def create_product(product: dict, db: Session = Depends(get_db)):
    db_product = Product(name=product["name"], price=product["price"])
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return {
        "id": db_product.id,
        "name": db_product.name,
        "price": db_product.price
    }


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

