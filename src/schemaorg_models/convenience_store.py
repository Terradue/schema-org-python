from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class ConvenienceStore(Store):
    """
A convenience store.
    """
    type_: Literal['https://schema.org/ConvenienceStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ConvenienceStore'),serialization_alias='class') # type: ignore
