from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ProductReturnEnumeration(Enumeration):
    """
ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    """
    type_: Literal['https://schema.org/ProductReturnEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ProductReturnEnumeration'),serialization_alias='class') # type: ignore
