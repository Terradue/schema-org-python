from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """
An ocean (for example, the Pacific).
    """
    type_: Literal['https://schema.org/OceanBodyOfWater'] = Field(default='https://schema.org/OceanBodyOfWater', alias='@type', serialization_alias='@type') # type: ignore
