from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class Brand(Intangible):
    """
A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    """
    class_: Literal['https://schema.org/Brand'] = Field(default='https://schema.org/Brand', alias='@type', serialization_alias='@type') # type: ignore
    review: Optional[Union["Review", List["Review"]]] = Field(default=None, validation_alias=AliasChoices('review', 'https://schema.org/review'), serialization_alias='https://schema.org/review')
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(default=None, validation_alias=AliasChoices('aggregateRating', 'https://schema.org/aggregateRating'), serialization_alias='https://schema.org/aggregateRating')
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(default=None, validation_alias=AliasChoices('logo', 'https://schema.org/logo'), serialization_alias='https://schema.org/logo')
    @field_serializer('logo')
    def logo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    slogan: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'), serialization_alias='https://schema.org/slogan')
