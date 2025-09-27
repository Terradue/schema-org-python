from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """
Enumerates different price components that together make up the total price for an offered product.
    """
    class_: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
