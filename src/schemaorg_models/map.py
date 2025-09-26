from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Map(CreativeWork):
    """
A map.
    """
    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = Field(default=None,validation_alias=AliasChoices('mapType', 'https://schema.org/mapType'),serialization_alias='https://schema.org/mapType')
