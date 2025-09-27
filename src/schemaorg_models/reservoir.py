from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class Reservoir(BodyOfWater):
    """
A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    """
    type_: Literal['https://schema.org/Reservoir'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Reservoir'),serialization_alias='class') # type: ignore
