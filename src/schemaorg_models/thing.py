from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
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
    from .property_value import PropertyValue
    from .event import Event
    from .image_object import ImageObject
    from .action import Action
    from .creative_work import CreativeWork
    from .text_object import TextObject

class Thing(BaseModel):
    '''
    The most generic type of item.

    Attributes:
        additionalType: An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the
    use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org <a href="https://schema.org/docs/styleguide.html">style guide</a>.
        identifier: The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
        
        image: An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].
        url: URL of the item.
        disambiguatingDescription: A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
        description: A description of the item.
        mainEntityOfPage: Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
        sameAs: URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
        name: The name of the item.
        subjectOf: A CreativeWork or Event about this Thing.
        alternateName: An alias for the item.
        potentialAction: Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
    '''
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
    identifier: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], 'PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifier',
            'https://schema.org/identifier'
        ),
        serialization_alias='https://schema.org/identifier'
    )
    image: Optional[Union['ImageObject', List['ImageObject'], HttpUrl, List[HttpUrl]]] = Field(
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
    description: Optional[Union[str, List[str], 'TextObject', List['TextObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'description',
            'https://schema.org/description'
        ),
        serialization_alias='https://schema.org/description'
    )
    mainEntityOfPage: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
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
    subjectOf: Optional[Union['Event', List['Event'], 'CreativeWork', List['CreativeWork']]] = Field(
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
    potentialAction: Optional[Union['Action', List['Action']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'potentialAction',
            'https://schema.org/potentialAction'
        ),
        serialization_alias='https://schema.org/potentialAction'
    )
