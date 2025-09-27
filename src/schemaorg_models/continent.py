from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.landform import Landform


class Continent(Landform):
    """
One of the continents (for example, Europe or Africa).
    """
    type_: Literal['https://schema.org/Continent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Continent'),serialization_alias='class') # type: ignore
