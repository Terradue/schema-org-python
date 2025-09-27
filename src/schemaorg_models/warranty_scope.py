from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    class_: Literal['https://schema.org/WarrantyScope'] = Field('class', alias='class', serialization_alias='class') # type: ignore
