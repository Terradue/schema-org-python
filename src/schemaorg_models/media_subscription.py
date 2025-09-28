from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

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
from schemaorg_models.organization import Organization

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
    authenticator: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'authenticator',
            'https://schema.org/authenticator'
        ),
        serialization_alias='https://schema.org/authenticator'
    )
