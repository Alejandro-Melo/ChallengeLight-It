from typing import List
from dotenv import load_dotenv
import os

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType, NameEmail
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
import logging

logger = logging.getLogger('mail-handler')

# Load environment variables from .env file
load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME", ""),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", ""),
    MAIL_FROM=os.getenv("MAIL_FROM", "noreply@mail.com"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 1025)),
    MAIL_SERVER=os.getenv("MAIL_SERVER", "mailpit"),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS", "False").lower() == "true",
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS", "False").lower() == "true",
    USE_CREDENTIALS=os.getenv("USE_CREDENTIALS", "False").lower() == "true",
    VALIDATE_CERTS=os.getenv("VALIDATE_CERTS", "False").lower() == "true"
)


app = FastAPI()

html = """
<h1>Confirmation mail<h1>
<p>The patient has been succesfully created!</p> 
"""
async def send_notification(email: List[str]):
    """Given a list of emails, sends a confirmation notification."""
    message = MessageSchema(
        subject="Mail for patient creation confirmation",
        recipients=email,  # Can include "Name <email@domain.com>" format
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        logger.info('Email sent successfully!')
    except Exception as e:
        logger.error(f"Error: \n{e}")
        return None
    return None