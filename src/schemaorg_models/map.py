from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .map_category_type import MapCategoryType

class Map(CreativeWork):
    """
A map.
    """
    class_: Literal['https://schema.org/Map'] = Field( # type: ignore
        default='https://schema.org/Map',
        alias='@type',
        serialization_alias='@type'
    )
    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mapType',
            'https://schema.org/mapType'
        ),
        serialization_alias='https://schema.org/mapType'
    )
