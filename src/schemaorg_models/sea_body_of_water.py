from typing import Literal
from pydantic import Field
from schemaorg_models.body_of_water import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """
A sea (for example, the Caspian sea).
    """
    class_: Literal['https://schema.org/SeaBodyOfWater'] = Field(default='https://schema.org/SeaBodyOfWater', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
