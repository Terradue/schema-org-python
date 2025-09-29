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

class Collection(CreativeWork):
    '''
    A collection of items, e.g. creative works or products.

    Attributes:
        collectionSize: The number of items in the [[Collection]].
    '''
    class_: Literal['https://schema.org/Collection'] = Field( # type: ignore
        default='https://schema.org/Collection',
        alias='@type',
        serialization_alias='@type'
    )
    collectionSize: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
