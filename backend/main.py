import logging
from fastapi import FastAPI, BackgroundTasks, Form, UploadFile, File
from fastapi.responses import RedirectResponse
from .src.classes import Patient
from .util.functions import *
from .util.dbhandling import *
from pydantic import EmailStr, ValidationError
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Annotated

#Config setup
logger = logging.getLogger('main app')
app = FastAPI()
IMAGES = "../uploads/"

@app.post('/patients/')
async def create_patient(
      email: Annotated[EmailStr, Form()], 
      phone: Annotated[PhoneNumber, Form()], 
      name: Annotated[str, Form()],
      photo: Annotated[UploadFile, File()],
      background_tasks: BackgroundTasks
    ):

    try:
        #Creates the Patient object
        patient = Patient(email=email, name=name, phone=phone, photo=photo)
        #Uploads the photo and gets the path of the file
        path = await upload_photo(patient.photo, IMAGES)
        #Connects to the db
        connection = await connect_db()
        if not connection:
            return {"error": "Database connection failed"}
        #Setup the db, with the required table
        await setup(connection)
        #Run the add patient function, with the patient info and background_tasks for email sending
        await add_patient(connection, patient, path, background_tasks)
        logger.info('Finished the process Successfully!')
        return {"msg":"Patient added Successfuly!"}
    
    except ValidationError as e:
        return {"err": e}
    
@app.get('/')
async def redirect_to_patients():
    return RedirectResponse(url="/docs")
