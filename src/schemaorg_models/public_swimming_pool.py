from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """
A public swimming pool.
    """
    type_: Literal['https://schema.org/PublicSwimmingPool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PublicSwimmingPool'),serialization_alias='class') # type: ignore
