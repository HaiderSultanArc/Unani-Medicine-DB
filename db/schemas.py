from pydantic import BaseModel


class Disease(BaseModel):
    name_eng               : str | None = None
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    icd_code               : str | None = None
    description            : str | None = None


class Symptom(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Cause(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class TreatmentPrinciple(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Drug(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class RegimentalTherapy(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class PharmacoTherapy(BaseModel):
    name_eng               : str | None = None
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Diet(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None


class Prevention(BaseModel):
    name_eng               : str
    name_persian           : str | None = None
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str | None = None