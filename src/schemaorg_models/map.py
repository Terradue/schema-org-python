from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Map(CreativeWork):
    """
A map.
    """
    class_: Literal['https://schema.org/Map'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = Field(default=None,validation_alias=AliasChoices('mapType', 'https://schema.org/mapType'), serialization_alias='https://schema.org/mapType')
