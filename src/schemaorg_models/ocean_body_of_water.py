from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """
An ocean (for example, the Pacific).
    """
    type_: Literal['https://schema.org/OceanBodyOfWater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OceanBodyOfWater'),serialization_alias='class') # type: ignore
