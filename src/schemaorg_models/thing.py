from __future__ import annotations
from pydantic import (
    field_serializer,
    AliasChoices,
    BaseModel,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .action import Action
    from .creative_work import CreativeWork
    from .event import Event
    from .text_object import TextObject
    from .property_value import PropertyValue
    from .image_object import ImageObject

class Thing(BaseModel):
    """
The most generic type of item.
    """
    # global serializer for HttpUrl
    @field_serializer(HttpUrl, mode="plain")
    def serialize_httpurl(self, value: HttpUrl) -> str:
        return str(value)

    class_: Literal['https://schema.org/Thing'] = Field( # type: ignore
        default='https://schema.org/Thing',
        alias='@type',
        serialization_alias='@type'
    )
    additionalType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalType',
            'https://schema.org/additionalType'
        ),
        serialization_alias='https://schema.org/additionalType'
    )
    identifier: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], "PropertyValue", List["PropertyValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifier',
            'https://schema.org/identifier'
        ),
        serialization_alias='https://schema.org/identifier'
    )
    image: Optional[Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'image',
            'https://schema.org/image'
        ),
        serialization_alias='https://schema.org/image'
    )
    url: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'url',
            'https://schema.org/url'
        ),
        serialization_alias='https://schema.org/url'
    )
    disambiguatingDescription: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'disambiguatingDescription',
            'https://schema.org/disambiguatingDescription'
        ),
        serialization_alias='https://schema.org/disambiguatingDescription'
    )
    description: Optional[Union[str, List[str], "TextObject", List["TextObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'description',
            'https://schema.org/description'
        ),
        serialization_alias='https://schema.org/description'
    )
    mainEntityOfPage: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mainEntityOfPage',
            'https://schema.org/mainEntityOfPage'
        ),
        serialization_alias='https://schema.org/mainEntityOfPage'
    )
    sameAs: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sameAs',
            'https://schema.org/sameAs'
        ),
        serialization_alias='https://schema.org/sameAs'
    )
    name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'name',
            'https://schema.org/name'
        ),
        serialization_alias='https://schema.org/name'
    )
    subjectOf: Optional[Union["Event", List["Event"], "CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subjectOf',
            'https://schema.org/subjectOf'
        ),
        serialization_alias='https://schema.org/subjectOf'
    )
    alternateName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alternateName',
            'https://schema.org/alternateName'
        ),
        serialization_alias='https://schema.org/alternateName'
    )
    potentialAction: Optional[Union["Action", List["Action"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'potentialAction',
            'https://schema.org/potentialAction'
        ),
        serialization_alias='https://schema.org/potentialAction'
    )
