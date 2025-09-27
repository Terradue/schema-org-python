from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class BikeStore(Store):
    """
A bike store.
    """
    type_: Literal['https://schema.org/BikeStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BikeStore'),serialization_alias='class') # type: ignore
