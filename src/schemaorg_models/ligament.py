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

class Ligament(AnatomicalStructure):
    '''
    A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.
    '''
    class_: Literal['https://schema.org/Ligament'] = Field( # type: ignore
        default='https://schema.org/Ligament',
        alias='@type',
        serialization_alias='@type'
    )
