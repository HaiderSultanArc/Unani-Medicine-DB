import json

from fastapi import UploadFile

import functions.database as db
import functions.datastore as ds


def uploadJSONToDataStore(uploadFile: UploadFile):
    try:
        jsonFile = json.loads(uploadFile.file.read())
        ds.uploadJSONToDataStore(jsonFile)
        
        return {
            "success": True,
            "message": "Successfully converted JSON file to MongoDB.",
            "data": None
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to convert JSON file to MongoDB. {error}",
            "data": None
        }


# --------------------------------------------------


def getDiseaseFromDataStore(diseaseName: str):
    try:
        diseaseData = ds.getDiseaseFromDataStore(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched disease data from MongoDB.",
            "data": diseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch disease data from MongoDB. {error}",
            "data": None
        }


# --------------------------------------------------


def uploadJSONToDatabase(uploadFile: UploadFile):
    try:
        jsonFile = json.loads(uploadFile.file.read())
        db.uploadJSONToDatabase(jsonFile)
        
        return {
            "success": True,
            "message": "Successfully converted JSON file to Database.",
            "data": None
        }
    except TypeError as error:
        return {
            "success": False,
            "message": f"Failed to convert JSON file to Database. {error}",
            "data": None
        }


# --------------------------------------------------


def getDiseaseFromDB(diseaseName: str):
    try:
        diseaseData = db.getDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched disease from Database.",
            "data": diseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch disease from Database. {error}",
            "data": None
        }


def getSymptomFromDB(symptomName: str):
    try:
        symptomData = db.getSymptomFromDB(symptomName)
        
        return {
            "success": True,
            "message": "Successfully fetched symptom from Database.",
            "data": symptomData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch symptom from Database. {error}",
            "data": None
        }
    

def getCauseFromDB(causeName: str):
    try:
        causeData = db.getCauseFromDB(causeName)
        
        return {
            "success": True,
            "message": "Successfully fetched cause from Database.",
            "data": causeData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch cause from Database. {error}",
            "data": None
        }


def getTreatmentPrincipleFromDB(treatmentPrincipleName: str):
    try:
        treatmentPrincipleData = db.getTreatmentPrincipleFromDB(treatmentPrincipleName)
        
        return {
            "success": True,
            "message": "Successfully fetched treatment principle from Database.",
            "data": treatmentPrincipleData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch treatment principle from Database. {error}",
            "data": None
        }


def getDrugFromDB(drugName: str):
    try:
        drugData = db.getDrugFromDB(drugName)
        
        return {
            "success": True,
            "message": "Successfully fetched drug from Database.",
            "data": drugData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch drug from Database. {error}",
            "data": None
        }
    

def getRegimentalTherapyFromDB(regimentalTherapyName: str):
    try:
        regimentalTherapyData = db.getRegimentalTherapyFromDB(regimentalTherapyName)
        
        return {
            "success": True,
            "message": "Successfully fetched regimental therapy from Database.",
            "data": regimentalTherapyData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch regimental therapy from Database. {error}",
            "data": None
        }


def getPharmacoTherapyFromDB(pharmacoTherapyDescription: str):
    try:
        pharmacoTherapyData = db.getPharmacoTherapyFromDB(pharmacoTherapyDescription)
        
        return {
            "success": True,
            "message": "Successfully fetched pharmaco therapy from Database.",
            "data": pharmacoTherapyData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch pharmaco therapy from Database. {error}",
            "data": None
        }


def getDietFromDB(dietName: str):
    try:
        dietData = db.getDietFromDB(dietName)
        
        return {
            "success": True,
            "message": "Successfully fetched diet from Database.",
            "data": dietData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch diet from Database. {error}",
            "data": None
        }


def getPreventionFromDB(preventionName: str):
    try:
        preventionData = db.getPreventionFromDB(preventionName)
        
        return {
            "success": True,
            "message": "Successfully fetched prevention from Database.",
            "data": preventionData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch prevention from Database. {error}",
            "data": None
        }


def getSymptomsByDiseaseFromDB(diseaseName: str):
    try:
        symptomsByDiseaseData = db.getSymptomsByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched symptoms by disease from Database.",
            "data": symptomsByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch symptoms by disease from Database. {error}",
            "data": None
        }


def getCausesByDiseaseFromDB(diseaseName: str):
    try:
        causesByDiseaseData = db.getCausesByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched causes by disease from Database.",
            "data": causesByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch causes by disease from Database. {error}",
            "data": None
        }


def getTreatmentPrinciplesByDiseaseFromDB(diseaseName: str):
    try:
        treatmentPrinciplesByDiseaseData = db.getTreatmentPrinciplesByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched treatment principles by disease from Database.",
            "data": treatmentPrinciplesByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch treatment principles by disease from Database. {error}",
            "data": None
        }


def getDrugsByDiseaseFromDB(diseaseName: str):
    try:
        drugsByDiseaseData = db.getDrugsByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched drugs by disease from Database.",
            "data": drugsByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch drugs by disease from Database. {error}",
            "data": None
        }


def getRegimentalTherapiesByDiseaseFromDB(diseaseName: str):
    try:
        regimentalTherapiesByDiseaseData = db.getRegimentalTherapiesByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched regimental therapies by disease from Database.",
            "data": regimentalTherapiesByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch regimental therapies by disease from Database. {error}",
            "data": None
        }


def getPharmacoTherapiesByDiseaseFromDB(diseaseName: str):
    try:
        pharmacoTherapiesByDiseaseData = db.getPharmacoTherapiesByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched pharmaco therapies by disease from Database.",
            "data": pharmacoTherapiesByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch pharmaco therapies by disease from Database. {error}",
            "data": None
        }


def getDietsByDiseaseFromDB(diseaseName: str):
    try:
        dietsByDiseaseData = db.getDietsByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched diets by disease from Database.",
            "data": dietsByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch diets by disease from Database. {error}",
            "data": None
        }


def getPreventionsByDiseaseFromDB(diseaseName: str):
    try:
        preventionsByDiseaseData = db.getPreventionsByDiseaseFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched preventions by disease from Database.",
            "data": preventionsByDiseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch preventions by disease from Database. {error}",
            "data": None
        }


def getDiseaseDataFromDB(diseaseName: str):
    try:
        diseaseData = db.getDiseaseDataFromDB(diseaseName)
        
        return {
            "success": True,
            "message": "Successfully fetched disease data from Database.",
            "data": diseaseData
        }
    except Exception as error:
        return {
            "success": False,
            "message": f"Failed to fetch disease data from Database. {error}",
            "data": None
        }