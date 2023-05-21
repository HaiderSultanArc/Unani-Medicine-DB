from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import functions.database as db
import utils.handle as handle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload_utags_json_to_data_store")
def upload_json_to_data_store(uploadFile: UploadFile):
    return handle.uploadJSONToDataStore(uploadFile)


@app.post("/upload_utags_json_to_database")
def upload_json_to_database(uploadFile: UploadFile):
    return handle.uploadJSONToDatabase(uploadFile)