from typing import Literal
from pydantic import Field
from schemaorg_models.broadcast_service import BroadcastService


class RadioBroadcastService(BroadcastService):
    """
A delivery service through which radio content is provided via broadcast over the air or online.
    """
    type_: Literal['https://schema.org/RadioBroadcastService'] = Field(default='https://schema.org/RadioBroadcastService', alias='@type', serialization_alias='@type') # type: ignore
