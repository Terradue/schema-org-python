from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_organization import MedicalOrganization
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_specialty import MedicalSpecialty
    from .medical_procedure import MedicalProcedure
    from .medical_test import MedicalTest
    from .medical_therapy import MedicalTherapy

class MedicalClinic(MedicalOrganization):
    '''
    A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

    Attributes:
        availableService: A medical service available from this provider.
        medicalSpecialty: A medical specialty of the provider.
    '''
    class_: Literal['https://schema.org/MedicalClinic'] = Field( # type: ignore
        default='https://schema.org/MedicalClinic',
        alias='@type',
        serialization_alias='@type'
    )
    availableService: Optional[Union['MedicalProcedure', List['MedicalProcedure'], 'MedicalTherapy', List['MedicalTherapy'], 'MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableService',
            'https://schema.org/availableService'
        ),
        serialization_alias='https://schema.org/availableService'
    )
    medicalSpecialty: Optional[Union['MedicalSpecialty', List['MedicalSpecialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
