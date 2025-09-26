from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Collection(CreativeWork):
    """
A collection of items, e.g. creative works or products.
    """
    collectionSize: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('collectionSize', 'https://schema.org/collectionSize'),serialization_alias='https://schema.org/collectionSize')
