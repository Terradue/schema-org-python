from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

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
