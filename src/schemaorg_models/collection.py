from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Collection(CreativeWork):
    """
A collection of items, e.g. creative works or products.
    """
    class_: Literal['https://schema.org/Collection'] = Field(default='https://schema.org/Collection', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    collectionSize: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('collectionSize', 'https://schema.org/collectionSize'), serialization_alias='https://schema.org/collectionSize')
