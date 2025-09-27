from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class IndividualProduct(Product):
    """
A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """
    type_: Literal['https://schema.org/IndividualProduct'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IndividualProduct'),serialization_alias='class') # type: ignore
    serialNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('serialNumber', 'https://schema.org/serialNumber'),serialization_alias='https://schema.org/serialNumber')
