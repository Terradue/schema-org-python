from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Map(CreativeWork):
    """
A map.
    """
    type_: Literal['https://schema.org/Map'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Map'),serialization_alias='class') # type: ignore
    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = Field(default=None,validation_alias=AliasChoices('mapType', 'https://schema.org/mapType'),serialization_alias='https://schema.org/mapType')
