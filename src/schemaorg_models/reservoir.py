from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Reservoir(BodyOfWater):
    """
A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    """
    type_: Literal['https://schema.org/Reservoir'] = Field(default='https://schema.org/Reservoir', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
