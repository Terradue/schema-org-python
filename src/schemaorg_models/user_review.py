from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.review import Review

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UserReview(Review):
    """
A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    """
    class_: Literal['https://schema.org/UserReview'] = Field( # type: ignore
        default='https://schema.org/UserReview',
        alias='@type',
        serialization_alias='@type'
    )
