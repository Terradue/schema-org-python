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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_enumeration import MedicalEnumeration
    from .drug import Drug
    from .medical_device import MedicalDevice
    from .medical_sign import MedicalSign
    from .medical_condition import MedicalCondition

class MedicalTest(MedicalEntity):
    '''
    Any medical test, typically performed for diagnostic purposes.

    Attributes:
        affectedBy: Drugs that affect the test's results.
        signDetected: A sign detected by the test.
        usesDevice: Device used to perform the test.
        usedToDiagnose: A condition the test is used to diagnose.
        normalRange: Range of acceptable values for a typical patient, when applicable.
    '''
    class_: Literal['https://schema.org/MedicalTest'] = Field( # type: ignore
        default='https://schema.org/MedicalTest',
        alias='@type',
        serialization_alias='@type'
    )
    affectedBy: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'affectedBy',
            'https://schema.org/affectedBy'
        ),
        serialization_alias='https://schema.org/affectedBy'
    )
    signDetected: Optional[Union['MedicalSign', List['MedicalSign']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'signDetected',
            'https://schema.org/signDetected'
        ),
        serialization_alias='https://schema.org/signDetected'
    )
    usesDevice: Optional[Union['MedicalDevice', List['MedicalDevice']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usesDevice',
            'https://schema.org/usesDevice'
        ),
        serialization_alias='https://schema.org/usesDevice'
    )
    usedToDiagnose: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usedToDiagnose',
            'https://schema.org/usedToDiagnose'
        ),
        serialization_alias='https://schema.org/usedToDiagnose'
    )
    normalRange: Optional[Union['MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'normalRange',
            'https://schema.org/normalRange'
        ),
        serialization_alias='https://schema.org/normalRange'
    )
