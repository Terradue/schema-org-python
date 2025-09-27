from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ItemAvailability(Enumeration):
    """
A list of possible product availability options.
    """
    type_: Literal['https://schema.org/ItemAvailability'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ItemAvailability'),serialization_alias='class') # type: ignore
