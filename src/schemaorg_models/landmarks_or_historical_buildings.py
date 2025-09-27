from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class LandmarksOrHistoricalBuildings(Place):
    """
An historical landmark or building.
    """
    type_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LandmarksOrHistoricalBuildings'),serialization_alias='class') # type: ignore
