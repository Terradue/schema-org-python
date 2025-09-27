from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ItemAvailability(Enumeration):
    """
A list of possible product availability options.
    """
    class_: Literal['https://schema.org/ItemAvailability'] = Field(default='https://schema.org/ItemAvailability', alias='@type', serialization_alias='@type') # type: ignore
