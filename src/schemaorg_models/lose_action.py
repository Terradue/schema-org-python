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

class LoseAction(AchieveAction):
    """
The act of being defeated in a competitive activity.
    """
    class_: Literal['https://schema.org/LoseAction'] = Field( # type: ignore
        default='https://schema.org/LoseAction',
        alias='@type',
        serialization_alias='@type'
    )
    winner: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'winner',
            'https://schema.org/winner'
        ),
        serialization_alias='https://schema.org/winner'
    )
