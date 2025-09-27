from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """
Enumerates different price types, for example list price, invoice price, and sale price.
    """
    type_: Literal['https://schema.org/PriceTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PriceTypeEnumeration'),serialization_alias='class') # type: ignore
