from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class GardenStore(Store):
    """
A garden store.
    """
    type_: Literal['https://schema.org/GardenStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GardenStore'),serialization_alias='class') # type: ignore
