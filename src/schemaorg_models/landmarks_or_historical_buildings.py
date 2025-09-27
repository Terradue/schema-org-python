from typing import Literal
from pydantic import Field
from schemaorg_models.place import Place


class LandmarksOrHistoricalBuildings(Place):
    """
An historical landmark or building.
    """
    type_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field(default='https://schema.org/LandmarksOrHistoricalBuildings', alias='@type', serialization_alias='@type') # type: ignore
