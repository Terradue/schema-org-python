from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class FulfillmentTypeEnumeration(Enumeration):
    """
A type of product fulfillment.
    """
    type_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field(default='https://schema.org/FulfillmentTypeEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
