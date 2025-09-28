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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .offer import Offer
    from .organization import Organization

class MediaSubscription(Intangible):
    """
A subscription which allows a user to access media including audio, video, books, etc.
    """
    class_: Literal['https://schema.org/MediaSubscription'] = Field( # type: ignore
        default='https://schema.org/MediaSubscription',
        alias='@type',
        serialization_alias='@type'
    )
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectsAcceptanceOf',
            'https://schema.org/expectsAcceptanceOf'
        ),
        serialization_alias='https://schema.org/expectsAcceptanceOf'
    )
    authenticator: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'authenticator',
            'https://schema.org/authenticator'
        ),
        serialization_alias='https://schema.org/authenticator'
    )
