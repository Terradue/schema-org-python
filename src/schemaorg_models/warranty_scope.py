from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    type_: Literal['https://schema.org/WarrantyScope'] = Field(default='https://schema.org/WarrantyScope', alias='@type', serialization_alias='@type') # type: ignore
