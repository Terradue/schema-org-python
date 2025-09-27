from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.landform import Landform


class Volcano(Landform):
    """
A volcano, like Fujisan.
    """
    type_: Literal['https://schema.org/Volcano'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Volcano'),serialization_alias='class') # type: ignore
