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

class BrainStructure(AnatomicalStructure):
    '''
    Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    '''
    class_: Literal['https://schema.org/BrainStructure'] = Field( # type: ignore
        default='https://schema.org/BrainStructure',
        alias='@type',
        serialization_alias='@type'
    )
