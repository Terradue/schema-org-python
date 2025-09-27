from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Pond(BodyOfWater):
    """
A pond.
    """
    class_: Literal['https://schema.org/Pond'] = Field('class', alias='class', serialization_alias='class') # type: ignore
