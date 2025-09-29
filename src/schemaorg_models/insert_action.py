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
from .add_action import AddAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place

class InsertAction(AddAction):
    '''
    The act of adding at a specific location in an ordered collection.

    Attributes:
        toLocation: A sub property of location. The final location of the object or the agent after the action.
    '''
    class_: Literal['https://schema.org/InsertAction'] = Field( # type: ignore
        default='https://schema.org/InsertAction',
        alias='@type',
        serialization_alias='@type'
    )
    toLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
