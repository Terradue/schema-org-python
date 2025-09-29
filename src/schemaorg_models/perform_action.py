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
from .play_action import PlayAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    '''
    The act of participating in performance arts.

    Attributes:
        entertainmentBusiness: A sub property of location. The entertainment business where the action occurred.
    '''
    class_: Literal['https://schema.org/PerformAction'] = Field( # type: ignore
        default='https://schema.org/PerformAction',
        alias='@type',
        serialization_alias='@type'
    )
    entertainmentBusiness: Optional[Union['EntertainmentBusiness', List['EntertainmentBusiness']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
