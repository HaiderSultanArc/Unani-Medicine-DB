import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

import uuid

import db.models as models
import db.schemas as schemas


def addDiseaseToDB(diseaseData: schemas.Disease):
    """
    Adds a disease to the database
    ==============================
    Parameters:
    
            The database session
        disease: dict
            The disease to be added to the database
    ----------------
    Returns:
        New Disease ID
    """
    newDiseaseID = str(uuid.uuid4())
    
    newDisease = models.Disease(
        id=newDiseaseID,
        name_eng=diseaseData.name_eng,
        name_persian=diseaseData.name_persian,
        descriptoin=diseaseData.description
    )
    
    newDisease.save()
    
    return newDiseaseID


def addSymptomToDB(symptomData: schemas.Symptom):
    """
    Adds a symptom to the database
    ==============================
    Parameters:
    
            The database session
        symptom: dict
            The symptom to be added to the database
    ----------------
    Returns:
        New Symptom ID
    """
    newSymptomID = str(uuid.uuid4())
    
    newSymptom = models.Symptom(
        id=newSymptomID,
        name_eng=symptomData.name_eng,
        name_persian=symptomData.name_persian,
        descriptoin=symptomData.description,
    )
    
    newSymptom.save()
    
    return newSymptomID


def addCauseToDB(causeData: schemas.Cause):
    """
    Adds a cause to the database
    ==============================
    Parameters:
    
            The database session
        cause: dict
            The cause to be added to the database
    ----------------
    Returns:
        New Cause ID
    """
    newCauseID = str(uuid.uuid4())
    
    newCause = models.Cause(
        id=newCauseID,
        name_eng=causeData.name_eng,
        name_persian=causeData.name_persian,
        description=causeData.description,
    )
    
    newCause.save()
    
    return newCauseID


def addTreatmentPrincipleToDB(treatmentPrincipleData: schemas.TreatmentPrinciple):
    """
    Adds a treatment principle to the database
    ==============================
    Parameters:
    
            The database session
        treatmentPrinciple: dict
            The treatment principle to be added to the database
    ----------------
    Returns:
        New Treatment Principle ID
    """
    newTreatmentPrincipleID = str(uuid.uuid4())
    
    newTreatmentPrinciple = models.TreatmentPrinciple(
        id=newTreatmentPrincipleID,
        name_eng=treatmentPrincipleData.name_eng,
        name_persian=treatmentPrincipleData.name_persian,
        descriptoin=treatmentPrincipleData.description,
    )
    
    newTreatmentPrinciple.save()
    
    return newTreatmentPrincipleID


def addDrug(drugData: schemas.Drug):
    """
    Adds a drug to the database
    ==============================
    Parameters:
    
            The database session
        drug: dict
            The drug to be added to the database
    ----------------
    Returns:
        New Drug ID
    """
    newDrugID = str(uuid.uuid4())
    
    newDrug = models.Drug(
        id=newDrugID,
        name_eng=drugData.name_eng,
        name_persian=drugData.name_persian,
        descriptoin=drugData.description,
    )
    
    newDrug.save()
    
    return newDrugID


def addRegimentalTherapy(regimentalTherapyData: schemas.RegimentalTherapy):
    """
    Adds a regimental therapy to the database
    ==============================
    Parameters:
    
            The database session
        regimentalTherapy: dict
            The regimental therapy to be added to the database
    ----------------
    Returns:
        New Regimental Therapy ID
    """
    newRegimentalTherapyID = str(uuid.uuid4())
    
    newRegimentalTherapy = models.RegimentalTherapy(
        id=newRegimentalTherapyID,
        name_eng=regimentalTherapyData.name_eng,
        name_persian=regimentalTherapyData.name_persian,
        descriptoin=regimentalTherapyData.description,
    )
    
    newRegimentalTherapy.save()
    
    return newRegimentalTherapyID


def addPharmacoTherapy(pharmacoTherapyData: schemas.PharmacoTherapy):
    """
    Adds a pharmaco therapy to the database
    ==============================
    Parameters:
    
            The database session
        pharmacoTherapy: dict
            The pharmaco therapy to be added to the database
    ----------------
    Returns:
        New Pharmaco Therapy ID
    """
    newPharmacoTherapyID = str(uuid.uuid4())
    
    newPharmacoTherapy = models.PharmacoTherapy(
        id=newPharmacoTherapyID,
        name_eng=pharmacoTherapyData.name_eng,
        name_persian=pharmacoTherapyData.name_persian,
        descriptoin=pharmacoTherapyData.description,
    )
    
    newPharmacoTherapy.save()
    
    return newPharmacoTherapyID


def addDiet(dietData: schemas.Diet):
    """
    Adds a diet to the database
    ==============================
    Parameters:
    
            The database session
        diet: dict
            The diet to be added to the database
    ----------------
    Returns:
        New Diet ID
    """
    newDietID = str(uuid.uuid4())
    
    newDiet = models.Diet(
        id=newDietID,
        name_eng=dietData.name_eng,
        name_persian=dietData.name_persian,
        descriptoin=dietData.description,
    )
    
    newDiet.save()
    
    return newDietID


def addPrevention(preventionData: schemas.Prevention):
    """
    Adds a prevention to the database
    ==============================
    Parameters:
    
            The database session
        prevention: dict
            The prevention to be added to the database
    ----------------
    Returns:
        New Prevention ID
    """
    newPreventionID = str(uuid.uuid4())
    
    newPrevention = models.Prevention(
        id=newPreventionID,
        name_eng=preventionData.name_eng,
        name_persian=preventionData.name_persian,
        descriptoin=preventionData.description,
    )
    
    newPrevention.save()
    
    return newPreventionID


def addDiseaseSymptomToDB(diseaseID: str, symptomID: str):
    """
    Adds a disease symptom to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        symptomID: str
            The symptom ID
    ----------------
    Returns:
        None
    """
    disease = models.Disease.objects.filter(id=diseaseID).first()
    symptom = models.Symptom.objects.filter(id=symptomID).first()
    
    if disease and symptom:
        disease.symptoms.add(symptom)
        disease.save()


def addDiseaseCauseToDB(diseaseID: str, causeID: str):
    """
    Adds a disease cause to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        causeID: str
            The cause ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    cause = models.Cause.objects.filter(id=causeID).first()
    
    if disease and cause:
        disease.causes.add(cause)
        disease.save()


def addDiseaseTreatmentPrincipleToDB(diseaseID: str, treatmentPrincipleID: str):
    """
    Adds a disease treatment principle to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        treatmentPrincipleID: str
            The treatment principle ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    treatmentPrinciple = models.TreatmentPrinciple.objects.filter(id=treatmentPrincipleID).first()
    
    if disease and treatmentPrinciple:
        disease.treatment_principles.add(treatmentPrinciple)
        disease.save()


def addDiseaseDrugToDB(diseaseID: str, drugID: str):
    """
    Adds a disease drug to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        drugID: str
            The drug ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    drug = models.Drug.objects.filter(id=drugID).first()
    
    if disease and drug:
        disease.drugs.add(drug)
        disease.save()


def addDiseaseRegimentalTherapyToDB(diseaseID: str, regimentalTherapyID: str):
    """
    Adds a disease regimental therapy to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        regimentalTherapyID: str
            The regimental therapy ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    regimentalTherapy = models.RegimentalTherapy.objects.filter(id=regimentalTherapyID).first()
    
    if disease and regimentalTherapy:
        disease.regimental_therapies.add(regimentalTherapy)
        disease.save()


def addDiseasePharmacoTherapyToDB(diseaseID: str, pharmacoTherapyID: str):
    """
    Adds a disease pharmaco therapy to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        pharmacoTherapyID: str
            The pharmaco therapy ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    pharmacoTherapy = models.PharmacoTherapy.objects.filter(id=pharmacoTherapyID).first()
    
    if disease and pharmacoTherapy:
        disease.pharmaco_therapies.add(pharmacoTherapy)
        disease.save()


def addDiseaseDietToDB(diseaseID: str, dietID: str):
    """
    Adds a disease diet to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        dietID: str
            The diet ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    diet = models.Diet.objects.filter(id=dietID).first()
    
    if disease and diet:
        disease.diets.add(diet)
        disease.save()


def addDiseasePreventionToDB(diseaseID: str, preventionID: str):
    """
    Adds a disease prevention to the database
    ==============================
    Parameters:
    
            The database session
        diseaseID: str
            The disease ID
        preventionID: str
            The prevention ID
    ----------------
    Returns:
        None
    """
    
    disease = models.Disease.objects.filter(id=diseaseID).first()
    prevention = models.Prevention.objects.filter(id=preventionID).first()
    
    if disease and prevention:
        disease.preventions.add(prevention)
        disease.save()


def uploadDataToDatabase(diseasesFile: dict):
    """
    Uploads the data to the database
    ================================
    Parameters:
        file: dict
            The file to be uploaded to the database
    ----------------
    Returns:
        None
    """
    
    for item in diseasesFile['diseases']:
        print(f"{item.get('disease_eng')=}")
        
        diseaseData = schemas.Disease(
            name_eng=item.get('disease_eng')[0],
            name_persian=item.get('disease_persian')[0],
            description=item.get('disease_description')[0],
        )
        
        diseaseID = addDiseaseToDB(diseaseData)
        
        for symptom in item.symptom_eng:
            symptomID = addSymptomToDB(symptom)
            addDiseaseSymptomToDB(diseaseID, symptomID)
        
        for cause in item.causes:
            causeID = addCauseToDB(cause)
            addDiseaseCauseToDB(diseaseID, causeID)
        
        for treatmentPrinciple in item.treatmentPrinciples:
            treatmentPrincipleID = addTreatmentPrincipleToDB(treatmentPrinciple)
            addDiseaseTreatmentPrincipleToDB(diseaseID, treatmentPrincipleID)
        
        for drug in item.drugs:
            drugID = addDrug(drug)
            addDiseaseDrugToDB(diseaseID, drugID)
        
        for regimentalTherapy in item.regimentalTherapies:
            regimentalTherapyID = addRegimentalTherapy(regimentalTherapy)
            addDiseaseRegimentalTherapyToDB(diseaseID, regimentalTherapyID)
        
        for pharmacoTherapy in item.pharmacoTherapies:
            pharmacoTherapyID = addPharmacoTherapy(pharmacoTherapy)
            addDiseasePharmacoTherapyToDB(diseaseID, pharmacoTherapyID)
        
        for diet in item.diets:
            dietID = addDiet(diet)
            addDiseaseDietToDB(diseaseID, dietID)
        
        for prevention in item.preventions:
            preventionID = addPrevention(prevention)
            addDiseasePreventionToDB(diseaseID, preventionID)