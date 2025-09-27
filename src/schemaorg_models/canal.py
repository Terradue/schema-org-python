from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    type_: Literal['https://schema.org/Canal'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Canal'),serialization_alias='class') # type: ignore
