from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class WholesaleStore(Store):
    """
A wholesale store.
    """
    type_: Literal['https://schema.org/WholesaleStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WholesaleStore'),serialization_alias='class') # type: ignore
