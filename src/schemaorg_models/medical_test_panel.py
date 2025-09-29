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
from .medical_test import MedicalTest

class MedicalTestPanel(MedicalTest):
    '''
    Any collection of tests commonly ordered together.

    Attributes:
        subTest: A component test of the panel.
    '''
    class_: Literal['https://schema.org/MedicalTestPanel'] = Field( # type: ignore
        default='https://schema.org/MedicalTestPanel',
        alias='@type',
        serialization_alias='@type'
    )
    subTest: Optional[Union['MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
