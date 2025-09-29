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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .__class import _Class
    from .enumeration import Enumeration

class Property(Intangible):
    '''
    A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.

    Attributes:
        supersededBy: Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
        rangeIncludes: Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.
        inverseOf: Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the 'alumni' and 'alumniOf' properties are inverseOf each other. Some properties don't have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.
        domainIncludes: Relates a property to a class that is (one of) the type(s) the property is expected to be used on.
    '''
    class_: Literal['https://schema.org/Property'] = Field( # type: ignore
        default='https://schema.org/Property',
        alias='@type',
        serialization_alias='@type'
    )
    supersededBy: Optional[Union['Enumeration', List['Enumeration'], '_Class', List['_Class'], 'Property', List['Property']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy',
            'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy'
    )
    rangeIncludes: Optional[Union['_Class', List['_Class']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'rangeIncludes',
            'https://schema.org/rangeIncludes'
        ),
        serialization_alias='https://schema.org/rangeIncludes'
    )
    inverseOf: Optional[Union['Property', List['Property']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inverseOf',
            'https://schema.org/inverseOf'
        ),
        serialization_alias='https://schema.org/inverseOf'
    )
    domainIncludes: Optional[Union['_Class', List['_Class']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'domainIncludes',
            'https://schema.org/domainIncludes'
        ),
        serialization_alias='https://schema.org/domainIncludes'
    )
