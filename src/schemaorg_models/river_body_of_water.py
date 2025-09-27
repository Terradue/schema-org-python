from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.body_of_water import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """
A river (for example, the broad majestic Shannon).
    """
    type_: Literal['https://schema.org/RiverBodyOfWater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RiverBodyOfWater'),serialization_alias='class') # type: ignore
