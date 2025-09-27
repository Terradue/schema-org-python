from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """
Categories of physical activity, organized by physiologic classification.
    """
    type_: Literal['https://schema.org/PhysicalActivityCategory'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PhysicalActivityCategory'),serialization_alias='class') # type: ignore
