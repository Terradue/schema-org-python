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
    from .anatomical_system import AnatomicalSystem

class Vein(Vessel):
    '''
    A type of blood vessel that specifically carries blood to the heart.

    Attributes:
        regionDrained: The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.
        drainsTo: The vasculature that the vein drains into.
        tributary: The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.
    '''
    class_: Literal['https://schema.org/Vein'] = Field( # type: ignore
        default='https://schema.org/Vein',
        alias='@type',
        serialization_alias='@type'
    )
    regionDrained: Optional[Union['AnatomicalStructure', List['AnatomicalStructure'], 'AnatomicalSystem', List['AnatomicalSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'regionDrained',
            'https://schema.org/regionDrained'
        ),
        serialization_alias='https://schema.org/regionDrained'
    )
    drainsTo: Optional[Union['Vessel', List['Vessel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drainsTo',
            'https://schema.org/drainsTo'
        ),
        serialization_alias='https://schema.org/drainsTo'
    )
    tributary: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tributary',
            'https://schema.org/tributary'
        ),
        serialization_alias='https://schema.org/tributary'
    )
