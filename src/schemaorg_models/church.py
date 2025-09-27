from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Church(PlaceOfWorship):
    """
A church.
    """
    class_: Literal['https://schema.org/Church'] = Field('class', alias='class', serialization_alias='class') # type: ignore
