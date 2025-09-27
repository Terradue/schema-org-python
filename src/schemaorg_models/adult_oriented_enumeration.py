from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class AdultOrientedEnumeration(Enumeration):
    """
Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    """
    class_: Literal['https://schema.org/AdultOrientedEnumeration'] = Field(default='https://schema.org/AdultOrientedEnumeration', alias='class', serialization_alias='class') # type: ignore
