from __future__ import annotations
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
from .physician import Physician
from .medical_organization import MedicalOrganization

class IndividualPhysician(Physician):
    """
An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals use [[hospitalAffiliation]]. 
The [[practicesAt]] property can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc. where this physician practices.
    """
    class_: Literal['https://schema.org/IndividualPhysician'] = Field( # type: ignore
        default='https://schema.org/IndividualPhysician',
        alias='@type',
        serialization_alias='@type'
    )
    practicesAt: Optional[Union[MedicalOrganization, List[MedicalOrganization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'practicesAt',
            'https://schema.org/practicesAt'
        ),
        serialization_alias='https://schema.org/practicesAt'
    )
