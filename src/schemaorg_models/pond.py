from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class Pond(BodyOfWater):
    """
A pond.
    """
    type_: Literal['https://schema.org/Pond'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Pond'),serialization_alias='class') # type: ignore
