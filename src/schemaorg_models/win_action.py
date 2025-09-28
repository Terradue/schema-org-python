from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.achieve_action import AchieveAction

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
from schemaorg_models.person import Person

class WinAction(AchieveAction):
    """
The act of achieving victory in a competitive activity.
    """
    class_: Literal['https://schema.org/WinAction'] = Field( # type: ignore
        default='https://schema.org/WinAction',
        alias='@type',
        serialization_alias='@type'
    )
    loser: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loser',
            'https://schema.org/loser'
        ),
        serialization_alias='https://schema.org/loser'
    )
