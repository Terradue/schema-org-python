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

class MedicalRiskFactor(MedicalEntity):
    '''
    A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.

    Attributes:
        increasesRiskOf: The condition, complication, etc. influenced by this factor.
    '''
    class_: Literal['https://schema.org/MedicalRiskFactor'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskFactor',
        alias='@type',
        serialization_alias='@type'
    )
    increasesRiskOf: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
