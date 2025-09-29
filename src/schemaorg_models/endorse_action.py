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
from .react_action import ReactAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

class EndorseAction(ReactAction):
    '''
    An agent approves/certifies/likes/supports/sanctions an object.

    Attributes:
        endorsee: A sub property of participant. The person/organization being supported.
    '''
    class_: Literal['https://schema.org/EndorseAction'] = Field( # type: ignore
        default='https://schema.org/EndorseAction',
        alias='@type',
        serialization_alias='@type'
    )
    endorsee: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
