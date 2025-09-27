from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """
A lake (for example, Lake Pontrachain).
    """
    type_: Literal['https://schema.org/LakeBodyOfWater'] = Field(default='https://schema.org/LakeBodyOfWater', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
