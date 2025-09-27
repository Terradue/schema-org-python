from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """
A river (for example, the broad majestic Shannon).
    """
    type_: Literal['https://schema.org/RiverBodyOfWater'] = Field(default='https://schema.org/RiverBodyOfWater', alias='@type', serialization_alias='@type') # type: ignore
