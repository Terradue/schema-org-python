from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .publication_event import PublicationEvent

class OnDemandEvent(PublicationEvent):
    """
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
    class_: Literal['https://schema.org/OnDemandEvent'] = Field( # type: ignore
        default='https://schema.org/OnDemandEvent',
        alias='@type',
        serialization_alias='@type'
    )
