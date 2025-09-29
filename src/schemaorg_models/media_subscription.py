from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    A subscription which allows a user to access media including audio, video, books, etc.

    Attributes:
        expectsAcceptanceOf: An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
        authenticator: The Organization responsible for authenticating the user's subscription. For example, many media apps require a cable/satellite provider to authenticate your subscription before playing media.
    '''
    class_: Literal['https://schema.org/MediaSubscription'] = Field( # type: ignore
        default='https://schema.org/MediaSubscription',
        alias='@type',
        serialization_alias='@type'
    )
    expectsAcceptanceOf: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectsAcceptanceOf',
            'https://schema.org/expectsAcceptanceOf'
        ),
        serialization_alias='https://schema.org/expectsAcceptanceOf'
    )
    authenticator: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'authenticator',
            'https://schema.org/authenticator'
        ),
        serialization_alias='https://schema.org/authenticator'
    )
