from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class Waterfall(BodyOfWater):
    """
A waterfall, like Niagara.
    """
    type_: Literal['https://schema.org/Waterfall'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Waterfall'),serialization_alias='class') # type: ignore
