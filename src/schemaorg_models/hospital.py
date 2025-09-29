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
from .civic_structure import CivicStructure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_therapy import MedicalTherapy
    from .medical_specialty import MedicalSpecialty
    from .medical_test import MedicalTest
    from .dataset import Dataset
    from .cdcpmd_record import CDCPMDRecord
    from .medical_procedure import MedicalProcedure

class Hospital(CivicStructure):
    '''
    A hospital.

    Attributes:
        healthcareReportingData: Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of [[Dataset]].
        medicalSpecialty: A medical specialty of the provider.
        availableService: A medical service available from this provider.
    '''
    class_: Literal['https://schema.org/Hospital'] = Field( # type: ignore
        default='https://schema.org/Hospital',
        alias='@type',
        serialization_alias='@type'
    )
    healthcareReportingData: Optional[Union['Dataset', List['Dataset'], 'CDCPMDRecord', List['CDCPMDRecord']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthcareReportingData',
            'https://schema.org/healthcareReportingData'
        ),
        serialization_alias='https://schema.org/healthcareReportingData'
    )
    medicalSpecialty: Optional[Union['MedicalSpecialty', List['MedicalSpecialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalSpecialty',
            'https://schema.org/medicalSpecialty'
        ),
        serialization_alias='https://schema.org/medicalSpecialty'
    )
    availableService: Optional[Union['MedicalProcedure', List['MedicalProcedure'], 'MedicalTherapy', List['MedicalTherapy'], 'MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableService',
            'https://schema.org/availableService'
        ),
        serialization_alias='https://schema.org/availableService'
    )
