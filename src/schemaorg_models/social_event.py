from typing import Literal
from pydantic import Field
from schemaorg_models.event import Event


class SocialEvent(Event):
    """
Event type: Social event.
    """
    class_: Literal['https://schema.org/SocialEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
