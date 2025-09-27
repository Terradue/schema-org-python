from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ProductReturnEnumeration(Enumeration):
    """
ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    """
    class_: Literal['https://schema.org/ProductReturnEnumeration'] = Field(default='https://schema.org/ProductReturnEnumeration', alias='class', serialization_alias='class') # type: ignore
