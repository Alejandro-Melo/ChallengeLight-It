
from fastapi import FastAPI, Form, UploadFile, File
from typing import Annotated
import uuid
import logging
import os


logger = logging.getLogger('Auxiliar Functions')


async def upload_photo(photo: Annotated[UploadFile, File()], IMAGES):
    """
    Function that uploads images to the desired path.

    Parameters required: 
    Photo (UploadFile, file to be uploaded)
    IMAGES (Str, File path)
    
    Returns: Path where the photo has been uploaded.
    """
    # Ensure the directory exists
    os.makedirs(IMAGES, exist_ok=True)

    # Reads from received content
    try:
        contents = await photo.read()
        name = uuid.uuid4()
        file_path = os.path.join(IMAGES, f"{str(name)}.jpg")
        with open(file_path, "wb") as f:
            f.write(contents)
        logger.info('File uploaded!')
        return f'/{file_path}'
    except Exception as e:
        logger.error(f"Error: \n{e}")
        return None