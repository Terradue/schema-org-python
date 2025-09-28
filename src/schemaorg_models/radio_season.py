from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work_season import CreativeWorkSeason

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioSeason(CreativeWorkSeason):
    """
Season dedicated to radio broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/RadioSeason'] = Field( # type: ignore
        default='https://schema.org/RadioSeason',
        alias='@type',
        serialization_alias='@type'
    )
