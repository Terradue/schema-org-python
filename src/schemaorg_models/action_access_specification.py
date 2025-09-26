from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.media_subscription import MediaSubscription
from schemaorg_models.place import Place
from schemaorg_models.thing import Thing

class ActionAccessSpecification(Intangible):
    """
A set of requirements that must be fulfilled in order to perform an Action.
    """
    requiresSubscription: Optional[Union[bool, List[bool], MediaSubscription, List[MediaSubscription]]] = Field(default=None,validation_alias=AliasChoices('requiresSubscription', 'https://schema.org/requiresSubscription'),serialization_alias='https://schema.org/requiresSubscription')
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = Field(default=None,validation_alias=AliasChoices('expectsAcceptanceOf', 'https://schema.org/expectsAcceptanceOf'),serialization_alias='https://schema.org/expectsAcceptanceOf')
    eligibleRegion: Optional[Union["GeoShape", List["GeoShape"], str, List[str], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('eligibleRegion', 'https://schema.org/eligibleRegion'),serialization_alias='https://schema.org/eligibleRegion')
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('availabilityEnds', 'https://schema.org/availabilityEnds'),serialization_alias='https://schema.org/availabilityEnds')
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], "GeoShape", List["GeoShape"]]] = Field(default=None,validation_alias=AliasChoices('ineligibleRegion', 'https://schema.org/ineligibleRegion'),serialization_alias='https://schema.org/ineligibleRegion')
    availabilityStarts: Optional[Union[datetime, List[datetime], date, List[date], time, List[time]]] = Field(default=None,validation_alias=AliasChoices('availabilityStarts', 'https://schema.org/availabilityStarts'),serialization_alias='https://schema.org/availabilityStarts')
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('category', 'https://schema.org/category'),serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

