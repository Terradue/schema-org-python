from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class GenderType(Enumeration):
    """
An enumeration of genders.
    """
    type_: Literal['https://schema.org/GenderType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GenderType'),serialization_alias='class') # type: ignore
