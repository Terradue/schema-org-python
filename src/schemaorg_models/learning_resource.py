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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .alignment_object import AlignmentObject
    from .defined_term import DefinedTerm

class LearningResource(CreativeWork):
    '''
    The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

[[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

[[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.

    Attributes:
        educationalLevel: The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        educationalAlignment: An alignment to an established educational framework.

This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
        teaches: The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
        educationalUse: The purpose of a work in the context of education; for example, 'assignment', 'group work'.
        competencyRequired: Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.
        learningResourceType: The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
        assesses: The item being described is intended to assess the competency or learning outcome defined by the referenced term.
    '''
    class_: Literal['https://schema.org/LearningResource'] = Field( # type: ignore
        default='https://schema.org/LearningResource',
        alias='@type',
        serialization_alias='@type'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    educationalAlignment: Optional[Union['AlignmentObject', List['AlignmentObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    teaches: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    educationalUse: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    competencyRequired: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    learningResourceType: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    assesses: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
