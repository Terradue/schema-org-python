from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """
Categories of physical activity, organized by physiologic classification.
    """
    class_: Literal['https://schema.org/PhysicalActivityCategory'] = Field('class', alias='class', serialization_alias='class') # type: ignore
