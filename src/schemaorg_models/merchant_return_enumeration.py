from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """
Enumerates several kinds of product return policies.
    """
    type_: Literal['https://schema.org/MerchantReturnEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MerchantReturnEnumeration'),serialization_alias='class') # type: ignore
