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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .map_category_type import MapCategoryType

class Map(CreativeWork):
    '''
    A map.

    Attributes:
        mapType: Indicates the kind of Map, from the MapCategoryType Enumeration.
    '''
    class_: Literal['https://schema.org/Map'] = Field( # type: ignore
        default='https://schema.org/Map',
        alias='@type',
        serialization_alias='@type'
    )
    mapType: Optional[Union['MapCategoryType', List['MapCategoryType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
