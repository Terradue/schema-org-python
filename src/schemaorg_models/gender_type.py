from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GenderType(Enumeration):
    """
An enumeration of genders.
    """
    class_: Literal['https://schema.org/GenderType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
