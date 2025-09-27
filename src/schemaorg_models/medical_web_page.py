from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage

from schemaorg_models.medical_audience import MedicalAudience

class MedicalWebPage(WebPage):
    """
A web page that provides medical information.
    """
    type_: Literal['https://schema.org/MedicalWebPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalWebPage'),serialization_alias='class') # type: ignore
    medicalAudience: Optional[Union[MedicalAudience, List[MedicalAudience], "MedicalAudienceType", List["MedicalAudienceType"]]] = Field(default=None,validation_alias=AliasChoices('medicalAudience', 'https://schema.org/medicalAudience'),serialization_alias='https://schema.org/medicalAudience')
    aspect: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('aspect', 'https://schema.org/aspect'),serialization_alias='https://schema.org/aspect')
