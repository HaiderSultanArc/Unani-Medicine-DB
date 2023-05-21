import json

from fastapi import UploadFile

import functions.database as db
import functions.datastore as ds


def uploadJSONToDataStore(uploadFile: UploadFile):
    try:
        jsonFile = json.loads(uploadFile.file.read())
        ds.uploadToDataStore(jsonFile)
        
        return {
            "success": True,
            "message": "Successfully converted JSON file to MongoDB.",
            "data": None
        }
    except TypeError as error:
        return {
            "success": False,
            "message": f"Failed to convert JSON file to MongoDB. {error}",
            "data": None
        }


def uploadJSONToDatabase(uploadFile: UploadFile):
    try:
        jsonFile = json.loads(uploadFile.file.read())
        db.uploadDataToDatabase(jsonFile)
        
        return {
            "success": True,
            "message": "Successfully converted JSON file to PostgreSQL.",
            "data": None
        }
    except TypeError as error:
        return {
            "success": False,
            "message": f"Failed to convert JSON file to PostgreSQL. {error}",
            "data": None
        }