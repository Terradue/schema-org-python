from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Map(CreativeWork):
    """
A map.
    """
    type_: Literal['https://schema.org/Map'] = Field(default='https://schema.org/Map', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    mapType: Optional[Union["MapCategoryType", List["MapCategoryType"]]] = Field(default=None, validation_alias=AliasChoices('mapType', 'https://schema.org/mapType'), serialization_alias='https://schema.org/mapType')
