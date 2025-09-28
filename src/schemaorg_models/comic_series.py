from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.periodical import Periodical

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComicSeries(Periodical):
    """
A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer".
    """
    class_: Literal['https://schema.org/ComicSeries'] = Field( # type: ignore
        default='https://schema.org/ComicSeries',
        alias='@type',
        serialization_alias='@type'
    )
