from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Collection(CreativeWork):
    """
A collection of items, e.g. creative works or products.
    """
    class_: Literal['https://schema.org/Collection'] = Field(default='https://schema.org/Collection', alias='@type', serialization_alias='@type') # type: ignore
    collectionSize: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('collectionSize', 'https://schema.org/collectionSize'), serialization_alias='https://schema.org/collectionSize')
