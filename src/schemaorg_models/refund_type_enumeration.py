from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """
Enumerates several kinds of product return refund types.
    """
    type_: Literal['https://schema.org/RefundTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RefundTypeEnumeration'),serialization_alias='class') # type: ignore
