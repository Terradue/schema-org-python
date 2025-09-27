from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Pond(BodyOfWater):
    """
A pond.
    """
    type_: Literal['https://schema.org/Pond'] = Field(default='https://schema.org/Pond', alias='@type', serialization_alias='@type') # type: ignore
