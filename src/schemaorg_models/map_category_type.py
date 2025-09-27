from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MapCategoryType(Enumeration):
    """
An enumeration of several kinds of Map.
    """
    class_: Literal['https://schema.org/MapCategoryType'] = Field(default='https://schema.org/MapCategoryType', alias='class', serialization_alias='class') # type: ignore
