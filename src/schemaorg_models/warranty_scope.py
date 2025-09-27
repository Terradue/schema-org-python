from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    type_: Literal['https://schema.org/WarrantyScope'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WarrantyScope'),serialization_alias='class') # type: ignore
