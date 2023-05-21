import json

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import utils.secrets as secrets


def uploadJSONToDataStore(file: dict):
    """
    Uploads a JSON file to the database.
    ================================
    Parameters:
    -----------
        file (dict):
            description: The file to be uploaded.
            type: dict
    -----------
    Returns:
    --------
        flag:
            description: The flag indicating whether the upload was successful.
            type: bool
    --------
    """
    
    client = pymongo.MongoClient(secrets.MONGODB_ATLAS_URI)
    db = client[secrets.MONGODB_ATLAS_DB]
    diseases = db['diseases']
    
    diseases.insert_many(file['diseases'])
    
    client.close()
    
    return True


def getDiseaseFromDataStore(diseaseName: str):
    """
    Gets a disease from the database.
    ================================
    Parameters:
        diseaseName (str):
            description: The name of the disease to be retrieved.
            type: str
    -----------
    Returns:
    --------
        disease:
            description: The disease retrieved from the database.
            type: dict
    """
    
    client = pymongo.MongoClient(secrets.MONGODB_ATLAS_URI)
    db = client[secrets.MONGODB_ATLAS_DB]
    diseases = db['diseases']

    disease = diseases.find_one({'disease_persian': diseaseName})
    
    return json.dumps(disease, default=str, ensure_ascii=False)
    