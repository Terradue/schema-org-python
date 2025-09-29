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
from .web_content import WebContent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .health_aspect_enumeration import HealthAspectEnumeration

class HealthTopicContent(WebContent):
    '''
    [[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.
  

    Attributes:
        hasHealthAspect: Indicates the aspect or aspects specifically addressed in some [[HealthTopicContent]]. For example, that the content is an overview, or that it talks about treatment, self-care, treatments or their side-effects.
    '''
    class_: Literal['https://schema.org/HealthTopicContent'] = Field( # type: ignore
        default='https://schema.org/HealthTopicContent',
        alias='@type',
        serialization_alias='@type'
    )
    hasHealthAspect: Optional[Union['HealthAspectEnumeration', List['HealthAspectEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
