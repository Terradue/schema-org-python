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
from .assess_action import AssessAction

class ChooseAction(AssessAction):
    """
The act of expressing a preference from a set of options or a large or unbounded set of choices/options.
    """
    class_: Literal['https://schema.org/ChooseAction'] = Field( # type: ignore
        default='https://schema.org/ChooseAction',
        alias='@type',
        serialization_alias='@type'
    )
    option: Optional[Union[str, List[str], Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'option',
            'https://schema.org/option'
        ),
        serialization_alias='https://schema.org/option'
    )
    actionOption: Optional[Union[str, List[str], Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionOption',
            'https://schema.org/actionOption'
        ),
        serialization_alias='https://schema.org/actionOption'
    )
