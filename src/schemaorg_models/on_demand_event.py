from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.publication_event import PublicationEvent

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OnDemandEvent(PublicationEvent):
    """
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
    class_: Literal['https://schema.org/OnDemandEvent'] = Field( # type: ignore
        default='https://schema.org/OnDemandEvent',
        alias='@type',
        serialization_alias='@type'
    )
