from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    class_: Literal['https://schema.org/Canal'] = Field('class', alias='class', serialization_alias='class') # type: ignore
