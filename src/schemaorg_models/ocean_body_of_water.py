from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """
An ocean (for example, the Pacific).
    """
    class_: Literal['https://schema.org/OceanBodyOfWater'] = Field(default='https://schema.org/OceanBodyOfWater', alias='class', serialization_alias='class') # type: ignore
