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
from .people_audience import PeopleAudience

class ParentAudience(PeopleAudience):
    '''
    A set of characteristics describing parents, who can be interested in viewing some content.

    Attributes:
        childMaxAge: Maximal age of the child.
        childMinAge: Minimal age of the child.
    '''
    class_: Literal['https://schema.org/ParentAudience'] = Field( # type: ignore
        default='https://schema.org/ParentAudience',
        alias='@type',
        serialization_alias='@type'
    )
    childMaxAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'childMaxAge',
            'https://schema.org/childMaxAge'
        ),
        serialization_alias='https://schema.org/childMaxAge'
    )
    childMinAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'childMinAge',
            'https://schema.org/childMinAge'
        ),
        serialization_alias='https://schema.org/childMinAge'
    )
