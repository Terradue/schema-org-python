from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ProductReturnEnumeration(Enumeration):
    """
ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    """
    type_: Literal['https://schema.org/ProductReturnEnumeration'] = Field(default='https://schema.org/ProductReturnEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
