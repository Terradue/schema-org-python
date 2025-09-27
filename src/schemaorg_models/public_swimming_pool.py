from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """
A public swimming pool.
    """
    class_: Literal['https://schema.org/PublicSwimmingPool'] = Field(default='https://schema.org/PublicSwimmingPool', alias='@type', serialization_alias='@type') # type: ignore
