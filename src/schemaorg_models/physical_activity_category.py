from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """
Categories of physical activity, organized by physiologic classification.
    """
    type_: Literal['https://schema.org/PhysicalActivityCategory'] = Field(default='https://schema.org/PhysicalActivityCategory', alias='@type', serialization_alias='@type') # type: ignore
