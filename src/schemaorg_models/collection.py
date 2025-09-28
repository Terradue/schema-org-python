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

class Collection(CreativeWork):
    """
A collection of items, e.g. creative works or products.
    """
    class_: Literal['https://schema.org/Collection'] = Field( # type: ignore
        default='https://schema.org/Collection',
        alias='@type',
        serialization_alias='@type'
    )
    collectionSize: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'collectionSize',
            'https://schema.org/collectionSize'
        ),
        serialization_alias='https://schema.org/collectionSize'
    )
