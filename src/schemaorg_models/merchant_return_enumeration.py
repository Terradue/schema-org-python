from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """
Enumerates several kinds of product return policies.
    """
    class_: Literal['https://schema.org/MerchantReturnEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
