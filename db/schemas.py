from pydantic import BaseModel


class Disease(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    icd_code               : str | None = None
    description            : str


class Symptom(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Cause(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class TreatmentPrinciple(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Drug(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class RegimentalTherapy(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class PharmacoTherapy(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Diet(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str


class Prevention(BaseModel):
    name_eng               : str
    name_persian           : str
    name_urdu              : str | None = None
    name_urdu_roman        : str | None = None
    name_arabic            : str | None = None
    name_hindi             : str | None = None
    description            : str