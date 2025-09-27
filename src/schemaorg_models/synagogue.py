from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """
A synagogue.
    """
    type_: Literal['https://schema.org/Synagogue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Synagogue'),serialization_alias='class') # type: ignore
