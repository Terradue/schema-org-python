from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class IndividualProduct(Product):
    """
A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """
    serialNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('serialNumber', 'https://schema.org/serialNumber'),serialization_alias='https://schema.org/serialNumber')
