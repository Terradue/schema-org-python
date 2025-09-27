from typing import List, Literal, Optional, Union
from datetime import date
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.medical_entity import MedicalEntity

class MedicalGuideline(MedicalEntity):
    """
Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.
    """
    class_: Literal['https://schema.org/MedicalGuideline'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    guidelineSubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(default=None,validation_alias=AliasChoices('guidelineSubject', 'https://schema.org/guidelineSubject'), serialization_alias='https://schema.org/guidelineSubject')
    evidenceLevel: Optional[Union["MedicalEvidenceLevel", List["MedicalEvidenceLevel"]]] = Field(default=None,validation_alias=AliasChoices('evidenceLevel', 'https://schema.org/evidenceLevel'), serialization_alias='https://schema.org/evidenceLevel')
    evidenceOrigin: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('evidenceOrigin', 'https://schema.org/evidenceOrigin'), serialization_alias='https://schema.org/evidenceOrigin')
    guidelineDate: Optional[Union[date, List[date]]] = Field(default=None,validation_alias=AliasChoices('guidelineDate', 'https://schema.org/guidelineDate'), serialization_alias='https://schema.org/guidelineDate')
