from __future__ import annotations

from .update_action import UpdateAction    

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
from schemaorg_models.thing import Thing

class ReplaceAction(UpdateAction):
    """
The act of editing a recipient by replacing an old object with a new object.
    """
    class_: Literal['https://schema.org/ReplaceAction'] = Field( # type: ignore
        default='https://schema.org/ReplaceAction',
        alias='@type',
        serialization_alias='@type'
    )
    replacer: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'replacer',
            'https://schema.org/replacer'
        ),
        serialization_alias='https://schema.org/replacer'
    )
    replacee: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'replacee',
            'https://schema.org/replacee'
        ),
        serialization_alias='https://schema.org/replacee'
    )
