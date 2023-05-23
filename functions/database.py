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
    
    try:
        disease = models.Disease.objects.get(name_persian=diseaseData.name_persian)
        return disease.id
    except models.Disease.DoesNotExist:
        newDisease = models.Disease(
            id=newDiseaseID,
            name_persian=diseaseData.name_persian
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
    
    try:
        symptom = models.Symptom.objects.get(name_eng=symptomData.name_eng)
        return symptom.id
    except models.Symptom.DoesNotExist:
        newSymptom = models.Symptom(
            id=newSymptomID,
            name_eng=symptomData.name_eng
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
    
    try:
        cause = models.Cause.objects.get(name_eng=causeData.name_eng)
        return cause.id
    except models.Cause.DoesNotExist:
        newCause = models.Cause(
            id=newCauseID,
            name_eng=causeData.name_eng
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
    
    try:
        treatmentPrinciple = models.TreatmentPrinciple.objects.get(name_eng=treatmentPrincipleData.name_eng)
        return treatmentPrinciple.id
    except models.TreatmentPrinciple.DoesNotExist:
        newTreatmentPrinciple = models.TreatmentPrinciple(
            id=newTreatmentPrincipleID,
            name_eng=treatmentPrincipleData.name_eng
        )
        
        newTreatmentPrinciple.save()
        return newTreatmentPrincipleID


def addDrugToDB(drugData: schemas.Drug):
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
    
    try:
        drug = models.Drug.objects.get(name_eng=drugData.name_eng)
        return drug.id
    except models.Drug.DoesNotExist:
        newDrug = models.Drug(
            id=newDrugID,
            name_eng=drugData.name_eng
        )
        
        newDrug.save()
        return newDrugID


def addRegimentalTherapyToDB(regimentalTherapyData: schemas.RegimentalTherapy):
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
    
    try:
        regimentalTherapy = models.RegimentalTherapy.objects.get(name_eng=regimentalTherapyData.name_eng)
        return regimentalTherapy.id
    except models.RegimentalTherapy.DoesNotExist:
        newRegimentalTherapy = models.RegimentalTherapy(
            id=newRegimentalTherapyID,
            name_eng=regimentalTherapyData.name_eng
        )
        
        newRegimentalTherapy.save()
        return newRegimentalTherapyID


def addPharmacoTherapyToDB(pharmacoTherapyData: schemas.PharmacoTherapy):
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
    
    try:
        pharmacoTherapy = models.PharmacoTherapy.objects.get(description=pharmacoTherapyData.description)
        return pharmacoTherapy.id
    except models.PharmacoTherapy.DoesNotExist:
        newPharmacoTherapy = models.PharmacoTherapy(
            id=newPharmacoTherapyID,
            description=pharmacoTherapyData.description
        )
        
        newPharmacoTherapy.save()
        return newPharmacoTherapyID


def addDietToDB(dietData: schemas.Diet):
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
 
    try:
        diet = models.Diet.objects.get(name_eng=dietData.name_eng)
        return diet.id
    except models.Diet.DoesNotExist:
        newDiet = models.Diet(
            id=newDietID,
            name_eng=dietData.name_eng
        )
        
        newDiet.save()
        return newDietID


def addPreventionToDB(preventionData: schemas.Prevention):
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
    
    try:
        prevention = models.Prevention.objects.get(name_eng=preventionData.name_eng)
        return prevention.id
    except models.Prevention.DoesNotExist:
        newPrevention = models.Prevention(
            id=newPreventionID,
            name_eng=preventionData.name_eng
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


def addDiseaseDietToDB(diseaseID: str, dietID: str, dietType: str):
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
        disease.diets.add(diet, through_defaults={'diet_type': dietType})
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


def uploadJSONToDatabase(diseasesFile: dict):
    """
    Uploads the data to the database
    ================================
    Parameters:    file: dict
            The file to be uploaded to the database
    ----------------
    Returns:
        None
    """
    
    for item in diseasesFile['diseases']:
        diseaseData = schemas.Disease(
            name_persian=item.get('disease_persian')[0],
        )
        
        diseaseID = addDiseaseToDB(diseaseData)
        
        for symptom in item.get('symptom_eng'):
            symptomData = schemas.Symptom(
                name_eng=symptom
            )
            
            symptomID = addSymptomToDB(symptomData)
            addDiseaseSymptomToDB(diseaseID, symptomID)
        
        for cause in item.get('cause_eng'):
            causeData = schemas.Cause(
                name_eng=cause
            )
            
            causeID = addCauseToDB(causeData)
            addDiseaseCauseToDB(diseaseID, causeID)
        
        for treatmentPrinciple in item.get('principle_of_treatment'):
            treatmentPrincipleData = schemas.TreatmentPrinciple(
                name_eng=treatmentPrinciple
            )
            
            treatmentPrincipleID = addTreatmentPrincipleToDB(treatmentPrincipleData)
            addDiseaseTreatmentPrincipleToDB(diseaseID, treatmentPrincipleID)
        
        for drug in item.get('comp_drug'):
            drugData = schemas.Drug(
                name_eng=drug
            )
            
            drugID = addDrugToDB(drugData)
            addDiseaseDrugToDB(diseaseID, drugID)
        
        for regimentalTherapy in item.get('reg_theropy'):
            regimentalTherapyData = schemas.RegimentalTherapy(
                name_eng=regimentalTherapy
            )
            
            regimentalTherapyID = addRegimentalTherapyToDB(regimentalTherapyData)
            addDiseaseRegimentalTherapyToDB(diseaseID, regimentalTherapyID)
        
        for pharmacoTherapy in item.get('pharmacotherapy'):
            pharmacoTherapyData = schemas.PharmacoTherapy(
                description=pharmacoTherapy
            )
            
            pharmacoTherapyID = addPharmacoTherapyToDB(pharmacoTherapyData)
            addDiseasePharmacoTherapyToDB(diseaseID, pharmacoTherapyID)
        
        for diet in item.get('diet_recom'):
            dietData = schemas.Diet(
                name_eng=diet
            )
            
            dietID = addDietToDB(dietData)
            addDiseaseDietToDB(diseaseID, dietID, dietType='recommended')
        
        for diet in item.get('diet_restrict'):
            dietData = schemas.Diet(
                name_eng=diet
            )
            
            dietID = addDietToDB(dietData)
            addDiseaseDietToDB(diseaseID, dietID, dietType='restricted')
        
        for prevention in item.get('prevention'):
            preventionData = schemas.Prevention(
                name_eng=prevention
            )
            
            preventionID = addPreventionToDB(preventionData)
            addDiseasePreventionToDB(diseaseID, preventionID)


# ------------------------------ #


def getDiseaseFromDB(diseaseName: str):
    """
    Gets the disease from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        disease: Disease
            The disease object
    """
    disease = models.Disease.objects.filter(name_persian__icontains=diseaseName).first()
    
    return disease


def getSymptomFromDB(symptomName: str):
    """
    Gets the symptom from the database
    ==============================
    Parameters:
            The database session
        symptomName: str
            The symptom name
    ----------------
    Returns:
        symptom: Symptom
            The symptom object
    """
    symptom = models.Symptom.objects.filter(name_eng__icontains=symptomName).first()
    
    return symptom


def getCauseFromDB(causeName: str):
    """
    Gets the cause from the database
    ==============================
    Parameters:
            The database session
        causeName: str
            The cause name
    ----------------
    Returns:
        cause: Cause
            The cause object
    """
    cause = models.Cause.objects.filter(name_eng__icontains=causeName).first()
    
    return cause


def getTreatmentPrincipleFromDB(treatmentPrincipleName: str):
    """
    Gets the treatment principle from the database
    ==============================
    Parameters:
            The database session
        treatmentPrincipleName: str
            The treatment principle name
    ----------------
    Returns:
        treatmentPrinciple: TreatmentPrinciple
            The treatment principle object
    """
    treatmentPrinciple = models.TreatmentPrinciple.objects.filter(name_eng__icontains=treatmentPrincipleName).first()
    
    return treatmentPrinciple


def getDrugFromDB(drugName: str):
    """
    Gets the drug from the database
    ==============================
    Parameters:
            The database session
        drugName: str
            The drug name
    ----------------
    Returns:
        drug: Drug
            The drug object
    """
    drug = models.Drug.objects.filter(name_eng__icontains=drugName).first()
    
    return drug


def getRegimentalTherapyFromDB(regimentalTherapyName: str):
    """
    Gets the regimental therapy from the database
    ==============================
    Parameters:
            The database session
        regimentalTherapyName: str
            The regimental therapy name
    ----------------
    Returns:
        regimentalTherapy: RegimentalTherapy
            The regimental therapy object
    """
    regimentalTherapy = models.RegimentalTherapy.objects.filter(name_eng__icontains=regimentalTherapyName).first()
    
    return regimentalTherapy


def getPharmacoTherapyFromDB(pharmacoTherapyDescription: str):
    """
    Gets the pharmaco therapy from the database
    ==============================
    Parameters:
            The database session
        pharmacoTherapyDescription: str
            The pharmaco therapy description
    ----------------
    Returns:
        pharmacoTherapy: PharmacoTherapy
            The pharmaco therapy object
    """
    pharmacoTherapy = models.PharmacoTherapy.objects.filter(description__icontains=pharmacoTherapyDescription).first()
    
    return pharmacoTherapy


def getDietFromDB(dietName: str):
    """
    Gets the diet from the database
    ==============================
    Parameters:
            The database session
        dietName: str
            The diet name
    ----------------
    Returns:
        diet: Diet
            The diet object
    """
    diet = models.Diet.objects.filter(name_eng__icontains=dietName).first()
    
    return diet


def getPreventionFromDB(preventionName: str):
    """
    Gets the prevention from the database
    ==============================
    Parameters:
            The database session
        preventionName: str
            The prevention name
    ----------------
    Returns:
        prevention: Prevention
            The prevention object
    """
    prevention = models.Prevention.objects.filter(name_eng__icontains=preventionName).first()
    
    return prevention


def getSymptomsByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease symptoms from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseSymptoms: List[Symptom]
            The disease symptoms
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseSymptoms = disease.symptoms.all()
        return diseaseSymptoms
    
    return []


def getCausesByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease causes from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseCauses: List[Cause]
            The disease causes
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseCauses = disease.causes.all()
        return diseaseCauses
    
    return []


def getTreatmentPrinciplesByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease treatment principles from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseTreatmentPrinciples: List[TreatmentPrinciple]
            The disease treatment principles
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseTreatmentPrinciples = disease.treatment_principles.all()
        return diseaseTreatmentPrinciples
    
    return []


def getDrugsByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease drugs from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseDrugs: List[Drug]
            The disease drugs
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseDrugs = disease.drugs.all()
        return diseaseDrugs
    
    return []


def getRegimentalTherapiesByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease regimental therapies from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseRegimentalTherapies: List[RegimentalTherapy]
            The disease regimental therapies
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseRegimentalTherapies = disease.regimental_therapies.all()
        return diseaseRegimentalTherapies
    
    return []


def getPharmacoTherapiesByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease pharmaco therapies from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseasePharmacoTherapies: List[PharmacoTherapy]
            The disease pharmaco therapies
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseasePharmacoTherapies = disease.pharmaco_therapies.all()
        return diseasePharmacoTherapies
    
    return []


def getDietsByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease diets from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseDiets: List[Diet]
            The disease diets
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseDiets = disease.diets.all()
        return diseaseDiets
    
    return []


def getPreventionsByDiseaseFromDB(diseaseName: str):
    """
    Gets the disease preventions from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseasePreventions: List[Prevention]
            The disease preventions
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseasePreventions = disease.preventions.all()
        return diseasePreventions
    
    return []


def getDiseaseDataFromDB(diseaseName: str):
    """
    Gets the disease data from the database
    ==============================
    Parameters:
            The database session
        diseaseName: str
            The disease name
    ----------------
    Returns:
        diseaseData: Dict
            The disease data
    """
    disease = getDiseaseFromDB(diseaseName)
    
    if disease:
        diseaseData = {
            'dis_name_eng': [disease.name_eng],
            'disease_persian': [disease.name_persian],
            'disease_urdu': [disease.name_urdu],
            'disease_urdu_roman': [disease.name_urdu_roman],
            'disease_arabic': [disease.name_arabic],
            'disease_hindi': [disease.name_hindi],
            'disease_description': [disease.description],
            'symptom_eng': [symptom.name_eng for symptom in disease.symptoms.all()],
            'symptom_persian': [symptom.name_persian for symptom in disease.symptoms.all()],
            'symptom_urdu': [symptom.name_urdu for symptom in disease.symptoms.all()],
            'symptom_urdu_roman': [symptom.name_urdu_roman for symptom in disease.symptoms.all()],
            'symptom_arabic': [symptom.name_arabic for symptom in disease.symptoms.all()],
            'symptom_hindi': [symptom.name_hindi for symptom in disease.symptoms.all()],
            'symptom_description': [symptom.description for symptom in disease.symptoms.all()],
            'cause_eng': [cause.name_eng for cause in disease.causes.all()],
            'cause_persian': [cause.name_persian for cause in disease.causes.all()],
            'cause_urdu': [cause.name_urdu for cause in disease.causes.all()],
            'cause_urdu_roman': [cause.name_urdu_roman for cause in disease.causes.all()],
            'cause_arabic': [cause.name_arabic for cause in disease.causes.all()],
            'cause_hindi': [cause.name_hindi for cause in disease.causes.all()],
            'cause_description': [cause.description for cause in disease.causes.all()],
            'principle_of_treatment': [treatment_principle.name_eng for treatment_principle in disease.treatment_principles.all()],
            'comp_drug': [drug.name_eng for drug in disease.drugs.all()],
            'reg_theropy': [regimental_therapy.name_eng for regimental_therapy in disease.regimental_therapies.all()],
            'pharmacotherapy': [pharmaco_therapy.description for pharmaco_therapy in disease.pharmaco_therapies.all()],
            'diet_recom': [diet.name_eng for diet in disease.diets.filter(diseasedietlink__diet_type='recommended')],
            'diet_restrict' : [diet.name_eng for diet in disease.diets.filter(diseasedietlink__diet_type='restricted')],
            'prevention': [prevention.name_eng for prevention in disease.preventions.all()]
        }
        
        return diseaseData
    
    return {}