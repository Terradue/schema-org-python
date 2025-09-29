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
    from .drug import Drug
    from .medical_device import MedicalDevice
    from .medical_enumeration import MedicalEnumeration
    from .medical_condition import MedicalCondition
    from .medical_sign import MedicalSign

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    signDetected: Optional[Union['MedicalSign', List['MedicalSign']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    usesDevice: Optional[Union['MedicalDevice', List['MedicalDevice']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    usedToDiagnose: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    normalRange: Optional[Union['MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
