from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Waterfall(BodyOfWater):
    """
A waterfall, like Niagara.
    """
    type_: Literal['https://schema.org/Waterfall'] = Field(default='https://schema.org/Waterfall', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
