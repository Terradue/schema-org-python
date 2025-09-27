from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class ToyStore(Store):
    """
A toy store.
    """
    type_: Literal['https://schema.org/ToyStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ToyStore'),serialization_alias='class') # type: ignore
