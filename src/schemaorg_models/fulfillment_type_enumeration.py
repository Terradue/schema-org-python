from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class FulfillmentTypeEnumeration(Enumeration):
    """
A type of product fulfillment.
    """
    type_: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FulfillmentTypeEnumeration'),serialization_alias='class') # type: ignore
