from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from fastapi import UploadFile, File
from typing import Optional
import logging

import logging

# ------------------------------------ MODELS ----------------------------------------------------

logger = logging.getLogger('model_verification')

class Patient(BaseModel):
    email: EmailStr
    name: str
    phone: PhoneNumber
    photo: UploadFile

# --------------------------- LOGGER -----------------------------------------------------

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
