from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class Brand(Intangible):
    """
A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    """
    review: Optional[Union["Review", List["Review"]]] = Field(default=None,validation_alias=AliasChoices('review', 'https://schema.org/review'),serialization_alias='https://schema.org/review')
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(default=None,validation_alias=AliasChoices('aggregateRating', 'https://schema.org/aggregateRating'),serialization_alias='https://schema.org/aggregateRating')
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None,validation_alias=AliasChoices('logo', 'https://schema.org/logo'),serialization_alias='https://schema.org/logo')
    slogan: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),serialization_alias='https://schema.org/slogan')
