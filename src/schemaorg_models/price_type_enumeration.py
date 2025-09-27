from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """
Enumerates different price types, for example list price, invoice price, and sale price.
    """
    class_: Literal['https://schema.org/PriceTypeEnumeration'] = Field(default='https://schema.org/PriceTypeEnumeration', alias='class', serialization_alias='class') # type: ignore
