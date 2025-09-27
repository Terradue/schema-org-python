from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    type_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReturnFeesEnumeration'),serialization_alias='class') # type: ignore
