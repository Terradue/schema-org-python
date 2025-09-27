from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """
A synagogue.
    """
    class_: Literal['https://schema.org/Synagogue'] = Field(default='https://schema.org/Synagogue', alias='class', serialization_alias='class') # type: ignore
