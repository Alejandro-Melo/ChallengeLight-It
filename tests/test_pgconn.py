import asyncio
import asyncpg
import os
from dotenv import load_dotenv
import os

load_dotenv()

async def test_postgresql_connection():
    """Test connection to PostgreSQL database using asyncpg."""
    try:
        connection = await asyncpg.connect(
            database=os.environ.get('PG_DB'),
            user=os.environ.get('PG_USER'),
            password=os.environ.get('PG_PASSWORD'),
            host=os.environ.get('PG_HOST'),
            port=os.environ.get('PG_PORT')
        )
        
        print("Connection to PostgreSQL database successful!")
        await connection.close()
    except Exception as e:
        print(f"Error: Unable to connect to the database\n{e}")

if __name__ == "__main__":
    asyncio.run(test_postgresql_connection())
