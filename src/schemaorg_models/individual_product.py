from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.product import Product


class IndividualProduct(Product):
    """
A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """
    class_: Literal['https://schema.org/IndividualProduct'] = Field(default='https://schema.org/IndividualProduct', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    serialNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('serialNumber', 'https://schema.org/serialNumber'), serialization_alias='https://schema.org/serialNumber')
