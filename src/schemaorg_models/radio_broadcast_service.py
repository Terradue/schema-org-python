from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.broadcast_service import BroadcastService


class RadioBroadcastService(BroadcastService):
    """
A delivery service through which radio content is provided via broadcast over the air or online.
    """
    type_: Literal['https://schema.org/RadioBroadcastService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioBroadcastService'),serialization_alias='class') # type: ignore
