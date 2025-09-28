from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .thing import Thing
from .action import Action

class UpdateAction(Action):
    """
The act of managing by changing/editing the state of the object.
    """
    class_: Literal['https://schema.org/UpdateAction'] = Field( # type: ignore
        default='https://schema.org/UpdateAction',
        alias='@type',
        serialization_alias='@type'
    )
    targetCollection: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetCollection',
            'https://schema.org/targetCollection'
        ),
        serialization_alias='https://schema.org/targetCollection'
    )
    collection: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'collection',
            'https://schema.org/collection'
        ),
        serialization_alias='https://schema.org/collection'
    )
