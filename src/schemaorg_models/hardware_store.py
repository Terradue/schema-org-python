from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class HardwareStore(Store):
    """
A hardware store.
    """
    type_: Literal['https://schema.org/HardwareStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HardwareStore'),serialization_alias='class') # type: ignore
