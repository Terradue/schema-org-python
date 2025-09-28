from __future__ import annotations

from .medical_intangible import MedicalIntangible    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.administrative_area import AdministrativeArea

class DrugLegalStatus(MedicalIntangible):
    """
The legal availability status of a medical drug.
    """
    class_: Literal['https://schema.org/DrugLegalStatus'] = Field( # type: ignore
        default='https://schema.org/DrugLegalStatus',
        alias='@type',
        serialization_alias='@type'
    )
    applicableLocation: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicableLocation',
            'https://schema.org/applicableLocation'
        ),
        serialization_alias='https://schema.org/applicableLocation'
    )
