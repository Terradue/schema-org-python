from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """
Enumerates different price components that together make up the total price for an offered product.
    """
    class_: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field(default='https://schema.org/PriceComponentTypeEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
