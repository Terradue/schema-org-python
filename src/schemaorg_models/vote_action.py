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
from .choose_action import ChooseAction
from .person import Person

class VoteAction(ChooseAction):
    """
The act of expressing a preference from a fixed/finite/structured set of choices/options.
    """
    class_: Literal['https://schema.org/VoteAction'] = Field( # type: ignore
        default='https://schema.org/VoteAction',
        alias='@type',
        serialization_alias='@type'
    )
    candidate: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'candidate',
            'https://schema.org/candidate'
        ),
        serialization_alias='https://schema.org/candidate'
    )
