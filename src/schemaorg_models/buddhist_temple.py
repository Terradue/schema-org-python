from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """
A Buddhist temple.
    """
    type_: Literal['https://schema.org/BuddhistTemple'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BuddhistTemple'),serialization_alias='class') # type: ignore
