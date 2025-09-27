from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """
A Hindu temple.
    """
    type_: Literal['https://schema.org/HinduTemple'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HinduTemple'),serialization_alias='class') # type: ignore
