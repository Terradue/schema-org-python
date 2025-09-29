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
from .react_action import ReactAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

class EndorseAction(ReactAction):
    """
An agent approves/certifies/likes/supports/sanctions an object.
    """
    class_: Literal['https://schema.org/EndorseAction'] = Field( # type: ignore
        default='https://schema.org/EndorseAction',
        alias='@type',
        serialization_alias='@type'
    )
    endorsee: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endorsee',
            'https://schema.org/endorsee'
        ),
        serialization_alias='https://schema.org/endorsee'
    )
