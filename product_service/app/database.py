from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/ecommerce"
# DATABASE_URL = "postgresql://localhost/ecommerce"
DATABASE_URL = "postgresql://ecommerce_user:mypassword123@localhost:5432/ecommerce"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()