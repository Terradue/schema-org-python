from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """
A lake (for example, Lake Pontrachain).
    """
    type_: Literal['https://schema.org/LakeBodyOfWater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LakeBodyOfWater'),serialization_alias='class') # type: ignore
