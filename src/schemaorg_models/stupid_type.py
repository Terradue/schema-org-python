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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class StupidType(Thing):
    '''
    A StupidType for testing.

    Attributes:
        stupidProperty: This is a StupidProperty! - for testing only.
    '''
    class_: Literal['https://schema.org/StupidType'] = Field( # type: ignore
        default='https://schema.org/StupidType',
        alias='@type',
        serialization_alias='@type'
    )
    stupidProperty: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
