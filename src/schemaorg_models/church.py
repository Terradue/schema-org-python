from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place_of_worship import PlaceOfWorship


class Church(PlaceOfWorship):
    """
A church.
    """
    type_: Literal['https://schema.org/Church'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Church'),serialization_alias='class') # type: ignore
