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
from .anatomical_structure import AnatomicalStructure

class Bone(AnatomicalStructure):
    '''
    Rigid connective tissue that comprises up the skeletal structure of the human body.
    '''
    class_: Literal['https://schema.org/Bone'] = Field( # type: ignore
        default='https://schema.org/Bone',
        alias='@type',
        serialization_alias='@type'
    )
