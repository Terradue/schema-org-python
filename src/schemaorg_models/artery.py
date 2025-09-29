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
from .vessel import Vessel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .anatomical_structure import AnatomicalStructure

class Artery(Vessel):
    '''
    A type of blood vessel that specifically carries blood away from the heart.

    Attributes:
        arterialBranch: The branches that comprise the arterial structure.
        supplyTo: The area to which the artery supplies blood.
    '''
    class_: Literal['https://schema.org/Artery'] = Field( # type: ignore
        default='https://schema.org/Artery',
        alias='@type',
        serialization_alias='@type'
    )
    arterialBranch: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'arterialBranch',
            'https://schema.org/arterialBranch'
        ),
        serialization_alias='https://schema.org/arterialBranch'
    )
    supplyTo: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supplyTo',
            'https://schema.org/supplyTo'
        ),
        serialization_alias='https://schema.org/supplyTo'
    )
