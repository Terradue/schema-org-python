from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class SizeGroupEnumeration(Enumeration):
    """
Enumerates common size groups for various product categories.
    """
    type_: Literal['https://schema.org/SizeGroupEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SizeGroupEnumeration'),serialization_alias='class') # type: ignore
