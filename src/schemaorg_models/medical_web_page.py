from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage

from schemaorg_models.medical_audience import MedicalAudience

class MedicalWebPage(WebPage):
    """
A web page that provides medical information.
    """
    class_: Literal['https://schema.org/MedicalWebPage'] = Field(default='https://schema.org/MedicalWebPage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    medicalAudience: Optional[Union[MedicalAudience, List[MedicalAudience], "MedicalAudienceType", List["MedicalAudienceType"]]] = Field(default=None, validation_alias=AliasChoices('medicalAudience', 'https://schema.org/medicalAudience'), serialization_alias='https://schema.org/medicalAudience')
    aspect: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('aspect', 'https://schema.org/aspect'), serialization_alias='https://schema.org/aspect')
