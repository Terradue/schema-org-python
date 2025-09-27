from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class FulfillmentTypeEnumeration(Enumeration):
    """
A type of product fulfillment.
    """
    class_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field(default='https://schema.org/FulfillmentTypeEnumeration', alias='class', serialization_alias='class') # type: ignore
