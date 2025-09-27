from typing import Literal
from pydantic import Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Church(PlaceOfWorship):
    """
A church.
    """
    type_: Literal['https://schema.org/Church'] = Field(default='https://schema.org/Church', alias='@type', serialization_alias='@type') # type: ignore
