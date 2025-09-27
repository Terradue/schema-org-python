from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class SocialEvent(Event):
    """
Event type: Social event.
    """
    type_: Literal['https://schema.org/SocialEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SocialEvent'),serialization_alias='class') # type: ignore
