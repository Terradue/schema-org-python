from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """
Enumerates several types of product return methods.
    """
    type_: Literal['https://schema.org/ReturnMethodEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReturnMethodEnumeration'),serialization_alias='class') # type: ignore
