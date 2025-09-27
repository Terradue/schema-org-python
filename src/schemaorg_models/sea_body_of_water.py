from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """
A sea (for example, the Caspian sea).
    """
    type_: Literal['https://schema.org/SeaBodyOfWater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SeaBodyOfWater'),serialization_alias='class') # type: ignore
