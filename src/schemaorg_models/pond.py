from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class Pond(BodyOfWater):
    """
A pond.
    """
    class_: Literal['https://schema.org/Pond'] = Field(default='https://schema.org/Pond', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
