import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import utils.secrets as secrets


def uploadToDataStore(file: dict):
    """
    Uploads a file to the database.
    ================================
    Parameters:
        file (dict): The file to be uploaded.
    ================================
    Returns:
        None
    """
    
    client = pymongo.MongoClient(secrets.MONGODB_ATLAS_URI)
    db = client[secrets.MONGODB_ATLAS_DB]
    diseases = db['diseases']
    
    diseases.insert_many(file['diseases'])
    
    client.close()