from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible

from schemaorg_models.administrative_area import AdministrativeArea

class DrugLegalStatus(MedicalIntangible):
    """
The legal availability status of a medical drug.
    """
    type_: Literal['https://schema.org/DrugLegalStatus'] = Field(default='https://schema.org/DrugLegalStatus', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    applicableLocation: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(default=None, validation_alias=AliasChoices('applicableLocation', 'https://schema.org/applicableLocation'), serialization_alias='https://schema.org/applicableLocation')
