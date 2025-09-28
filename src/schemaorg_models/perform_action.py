from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.play_action import PlayAction

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
from schemaorg_models.entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    """
The act of participating in performance arts.
    """
    class_: Literal['https://schema.org/PerformAction'] = Field( # type: ignore
        default='https://schema.org/PerformAction',
        alias='@type',
        serialization_alias='@type'
    )
    entertainmentBusiness: Optional[Union[EntertainmentBusiness, List[EntertainmentBusiness]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'entertainmentBusiness',
            'https://schema.org/entertainmentBusiness'
        ),
        serialization_alias='https://schema.org/entertainmentBusiness'
    )
