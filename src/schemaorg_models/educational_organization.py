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
from .civic_structure import CivicStructure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person

class EducationalOrganization(CivicStructure):
    '''
    An educational organization.

    Attributes:
        alumni: Alumni of an organization.
    '''
    class_: Literal['https://schema.org/EducationalOrganization'] = Field( # type: ignore
        default='https://schema.org/EducationalOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    alumni: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
