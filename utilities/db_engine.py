from sqlalchemy import create_engine

# PostgreSQL Database URL
DATABASE_URL = "postgresql+psycopg2://books:books@localhost:5432/books"

# Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL)
