from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """
Enumerates different price components that together make up the total price for an offered product.
    """
    type_: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PriceComponentTypeEnumeration'),serialization_alias='class') # type: ignore
