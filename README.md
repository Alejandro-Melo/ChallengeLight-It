# Light-it Challenge

## Features
- Patient creation endpoint, with:<br>
    - name
    - email
    - phone
    - photo
- Validations of all user-entered data
- presisting database in local volume
- asyncronous mail confirmation notification
- self-hosted mailpit instance for mail testing
- self-hosted pgadmin instance for easy database monitoring
- conteinarized main application for consistent and replicable development environment
- Docker compose for orchestration of containers and setting .env for all images

## How to run it:
- Use `docker compose up --build` for spinning up the containers
- in your browser, go to `localhost:8000`, you will see that the FastAPI docs appear
- Open the `/patients/` endpoint and use the "try it out" button, it will spawn a form for you to fill <br> **Important**, the phone number *HAS* to be real (i.e, +598 97 304 598), it is verified with a google lib that has a compilation of international numbers.
- After that, you will see that it returns an OK message, now we can go to the next part

## Checking the results
#### PgAdmin
- Go to `localhost:80` and login with the .env credentials correspondent to **pgAdmin**
- Then, you have to register the db, the host is the same as the pg container's name, and the password and user are in the .env file.
- After that, you go to db -> Databases -> mydb. 
- There, you left click the mydb and use "Query Tool".
- Use the following query: "SELECT * FROM patient", and now you will see the new records, with the correspondant patient data and timestamp of creation
#### Mailpit
- Simply go to `localhost:8025`, there you will see a new mail with the creation confirmation.
