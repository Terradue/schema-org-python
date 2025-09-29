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
from .medical_intangible import MedicalIntangible

class MedicalCode(MedicalIntangible):
    '''
    A code for a medical entity.

    Attributes:
        codingSystem: The coding system, e.g. 'ICD-10'.
        codeValue: A short textual code that uniquely identifies the value.
    '''
    class_: Literal['https://schema.org/MedicalCode'] = Field( # type: ignore
        default='https://schema.org/MedicalCode',
        alias='@type',
        serialization_alias='@type'
    )
    codingSystem: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codingSystem',
            'https://schema.org/codingSystem'
        ),
        serialization_alias='https://schema.org/codingSystem'
    )
    codeValue: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codeValue',
            'https://schema.org/codeValue'
        ),
        serialization_alias='https://schema.org/codeValue'
    )
