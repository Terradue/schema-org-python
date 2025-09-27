from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.organization import Organization

class MediaSubscription(Intangible):
    """
A subscription which allows a user to access media including audio, video, books, etc.
    """
    class_: Literal['https://schema.org/MediaSubscription'] = Field(default='https://schema.org/MediaSubscription', alias='class', serialization_alias='class') # type: ignore
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = Field(default=None, validation_alias=AliasChoices('expectsAcceptanceOf', 'https://schema.org/expectsAcceptanceOf'), serialization_alias='https://schema.org/expectsAcceptanceOf')
    authenticator: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('authenticator', 'https://schema.org/authenticator'), serialization_alias='https://schema.org/authenticator')
