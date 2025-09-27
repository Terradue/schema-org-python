from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    class_: Literal['https://schema.org/ItemListOrderType'] = Field(default='https://schema.org/ItemListOrderType', alias='class', serialization_alias='class') # type: ignore
