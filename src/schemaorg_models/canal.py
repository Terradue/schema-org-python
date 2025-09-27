from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Canal(BodyOfWater):
    """
A canal, like the Panama Canal.
    """
    type_: Literal['https://schema.org/Canal'] = Field(default='https://schema.org/Canal', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
