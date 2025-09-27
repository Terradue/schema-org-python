from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """
Enumerates several kinds of product return refund types.
    """
    class_: Literal['https://schema.org/RefundTypeEnumeration'] = Field(default='https://schema.org/RefundTypeEnumeration', alias='@type', serialization_alias='@type') # type: ignore
