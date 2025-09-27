from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """
A mosque.
    """
    type_: Literal['https://schema.org/Mosque'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Mosque'),serialization_alias='class') # type: ignore
