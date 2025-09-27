from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class SizeGroupEnumeration(Enumeration):
    """
Enumerates common size groups for various product categories.
    """
    class_: Literal['https://schema.org/SizeGroupEnumeration'] = Field(default='https://schema.org/SizeGroupEnumeration', alias='class', serialization_alias='class') # type: ignore
