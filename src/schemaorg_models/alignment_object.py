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

class AlignmentObject(Intangible):
    '''
    An intangible item that describes an alignment between a learning resource and a node in an educational framework.

Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.

    Attributes:
        alignmentType: A category of alignment between the learning resource and the framework node. Recommended values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'.
        targetName: The name of a node in an established educational framework.
        educationalFramework: The framework to which the resource being described is aligned.
        targetDescription: The description of a node in an established educational framework.
        targetUrl: The URL of a node in an established educational framework.
    '''
    class_: Literal['https://schema.org/AlignmentObject'] = Field( # type: ignore
        default='https://schema.org/AlignmentObject',
        alias='@type',
        serialization_alias='@type'
    )
    alignmentType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alignmentType',
            'https://schema.org/alignmentType'
        ),
        serialization_alias='https://schema.org/alignmentType'
    )
    targetName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetName',
            'https://schema.org/targetName'
        ),
        serialization_alias='https://schema.org/targetName'
    )
    educationalFramework: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalFramework',
            'https://schema.org/educationalFramework'
        ),
        serialization_alias='https://schema.org/educationalFramework'
    )
    targetDescription: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetDescription',
            'https://schema.org/targetDescription'
        ),
        serialization_alias='https://schema.org/targetDescription'
    )
    targetUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetUrl',
            'https://schema.org/targetUrl'
        ),
        serialization_alias='https://schema.org/targetUrl'
    )
