from sqlalchemy import create_engine, text

# PostgreSQL database credentials
DB_NAME = 'books'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://myuser:mypassword@localhost:5432/books')

def fetch_data():
    query = text("SELECT * FROM test_table")  # Replace 'your_table_name' with the actual table name
    with engine.connect() as connection:
        result = connection.execute(query)
        for row in result:
            print(row)
