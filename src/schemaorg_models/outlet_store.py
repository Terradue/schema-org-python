from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class OutletStore(Store):
    """
An outlet store.
    """
    type_: Literal['https://schema.org/OutletStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OutletStore'),serialization_alias='class') # type: ignore
