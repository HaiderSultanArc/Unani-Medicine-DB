from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import db.schemas as sc
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


@app.post("/get_disease_collection_from_data_store")
def get_disease_from_data_store(diseaseName: str):
    return handle.getDiseaseFromDataStore(diseaseName)


@app.post("/upload_utags_json_to_database")
def upload_json_to_database(uploadFile: UploadFile):
    return handle.uploadJSONToDatabase(uploadFile)


@app.post("/add_disease_to_db")
def add_disease_to_db(diseaseData: sc.Disease):
    return handle.addDiseaseToDB(diseaseData)


@app.post("/add_symptom_to_db")
def add_symptom_to_db(symptomData: sc.Symptom):
    return handle.addSymptomToDB(symptomData)


@app.post("/add_cause_to_db")
def add_cause_to_db(causeData: sc.Cause):
    return handle.addCauseToDB(causeData)


@app.post("/add_treatment_principle_to_db")
def add_treatment_principle_to_db(treatmentPrincipleData: sc.TreatmentPrinciple):
    return handle.addTreatmentPrincipleToDB(treatmentPrincipleData)


@app.post("/add_drug_to_db")
def add_drug_to_db(drugData: sc.Drug):
    return handle.addDrugToDB(drugData)


@app.post("/add_regimental_therapy_to_db")
def add_regimental_therapy_to_db(regimentalTherapyData: sc.RegimentalTherapy):
    return handle.addRegimentalTherapyToDB(regimentalTherapyData)


@app.post("/add_pharmacotherapy_to_db")
def add_pharmacotherapy_to_db(pharmacotherapyData: sc.PharmacoTherapy):
    return handle.addPharmacoTherapyToDB(pharmacotherapyData)


@app.post("/add_diet_to_db")
def add_diet_to_db(dietData: sc.Diet):
    return handle.addDietToDB(dietData)


@app.post("/add_prevention_to_db")
def add_prevention_to_db(preventionData: sc.Prevention):
    return handle.addPreventionToDB(preventionData)


@app.post("/get_disease_from_db")
def get_disease_from_db(diseaseName: str):
    return handle.getDiseaseFromDB(diseaseName)


@app.post("/get_symptom_from_db")
def get_symptom_from_db(symptomName: str):
    return handle.getSymptomFromDB(symptomName)


@app.post("/get_cause_from_db")
def get_cause_from_db(causeName: str):
    return handle.getCauseFromDB(causeName)


@app.post("/get_treatment_principle_from_db")
def get_treatment_principle_from_db(treatmentPrincipleName: str):
    return handle.getTreatmentPrincipleFromDB(treatmentPrincipleName)


@app.post("/get_drug_from_db")
def get_drug_from_db(drugName: str):
    return handle.getDrugFromDB(drugName)


@app.post("/get_regimental_therapy_from_db")
def get_regimental_therapy_from_db(regimentalTherapyName: str):
    return handle.getRegimentalTherapyFromDB(regimentalTherapyName)


@app.post("/get_pharmacotherapy_from_db")
def get_pharmacotherapy_from_db(pharmacotherapyDescription: str):
    return handle.getPharmacoTherapyFromDB(pharmacotherapyDescription)


@app.post("/get_diet_from_db")
def get_diet_from_db(dietName: str):
    return handle.getDietFromDB(dietName)


@app.post("/get_prevention_from_db")
def get_prevention_from_db(preventionName: str):
    return handle.getPreventionFromDB(preventionName)


@app.post("/get_symptoms_by_disease_from_db")
def get_symptoms_by_disease_from_db(diseaseName: str):
    return handle.getSymptomsByDiseaseFromDB(diseaseName)


@app.post("/get_causes_by_disease_from_db")
def get_causes_by_disease_from_db(diseaseName: str):
    return handle.getCausesByDiseaseFromDB(diseaseName)


@app.post("/get_treatment_principles_by_disease_from_db")
def get_treatment_principles_by_disease_from_db(diseaseName: str):
    return handle.getTreatmentPrinciplesByDiseaseFromDB(diseaseName)


@app.post("/get_drugs_by_disease_from_db")
def get_drugs_by_disease_from_db(diseaseName: str):
    return handle.getDrugsByDiseaseFromDB(diseaseName)


@app.post("/get_regimental_therapies_by_disease_from_db")
def get_regimental_therapies_by_disease_from_db(diseaseName: str):
    return handle.getRegimentalTherapiesByDiseaseFromDB(diseaseName)


@app.post("/get_pharmacotherapies_by_disease_from_db")
def get_pharmacotherapies_by_disease_from_db(diseaseName: str):
    return handle.getPharmacoTherapiesByDiseaseFromDB(diseaseName)


@app.post("/get_diets_by_disease_from_db")
def get_diets_by_disease_from_db(diseaseName: str):
    return handle.getDietsByDiseaseFromDB(diseaseName)


@app.post("/get_preventions_by_disease_from_db")
def get_preventions_by_disease_from_db(diseaseName: str):
    return handle.getPreventionsByDiseaseFromDB(diseaseName)


@app.post("/get_disease_data_from_db")
def get_disease_data_from_db(diseaseName: str):
    return handle.getDiseaseDataFromDB(diseaseName)