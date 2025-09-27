from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class AutoPartsStore(Store):
    """
An auto parts store.
    """
    type_: Literal['https://schema.org/AutoPartsStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoPartsStore'),serialization_alias='class') # type: ignore
