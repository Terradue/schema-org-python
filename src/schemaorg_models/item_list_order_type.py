from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    type_: Literal['https://schema.org/ItemListOrderType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ItemListOrderType'),serialization_alias='class') # type: ignore
