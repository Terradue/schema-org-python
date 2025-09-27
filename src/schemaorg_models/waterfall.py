from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Waterfall(BodyOfWater):
    """
A waterfall, like Niagara.
    """
    class_: Literal['https://schema.org/Waterfall'] = Field('class', alias='class', serialization_alias='class') # type: ignore
