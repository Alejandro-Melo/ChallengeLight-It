import os
from dotenv import load_dotenv
from fastapi import BackgroundTasks
import asyncpg
from .mailhandling import *
import logging

logger = logging.getLogger('db-handler')

# Load environment variables from .env file
load_dotenv()

async def connect_db():
    """Connect to the database and ensure the Patient table exists."""
    try:
        connection = await asyncpg.connect(
            database=os.environ.get('PG_DB'),
            user=os.environ.get('PG_USER'),
            password=os.environ.get('PG_PASSWORD'),
            host=os.environ.get('PG_HOST'),
            port=os.environ.get('PG_PORT')
        )
        logger.info('DB Connected Succesfully!')
        return connection
    except Exception as e:
        logger.error(f"Error: Unable to connect to the database\n{e}")
        return None

async def setup(connection):
    # Create the Patient table if it doesn't exist
    try:
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS Patient (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(50) NOT NULL,
                photo VARCHAR(255) NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        logger.info('Table created Succesfully!')
        return None
    except Exception as e:
        logger.error(f"Error: \n{e}")
        return None

async def add_patient(connection, patient, path, background_task: BackgroundTasks):
    """Insert a new Patient into the database."""
    try:
        await connection.execute(
            """
            INSERT INTO Patient (name, email, phone, photo)
            VALUES ($1, $2, $3, $4)
            """,
            patient.name,
            patient.email,
            patient.phone,
            path
        )
        logger.info('Patient inserted Succesfully!')
        background_task.add_task(send_notification, [os.environ.get('MAIL_TO')])
        return None
    except Exception as e:
        logger.error(f"Error: \n{e}")
        return None