from typing import Literal
from pydantic import Field
from schemaorg_models.place import Place


class LandmarksOrHistoricalBuildings(Place):
    """
An historical landmark or building.
    """
    class_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field(default='https://schema.org/LandmarksOrHistoricalBuildings', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
