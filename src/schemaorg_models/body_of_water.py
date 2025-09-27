from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class BodyOfWater(Landform):
    """
A body of water, such as a sea, ocean, or lake.
    """
    class_: Literal['https://schema.org/BodyOfWater'] = Field(default='https://schema.org/BodyOfWater', alias='class', serialization_alias='class') # type: ignore
