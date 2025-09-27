from typing import Literal
from pydantic import Field
from schemaorg_models.broadcast_channel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """
A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/RadioChannel'] = Field(default='https://schema.org/RadioChannel', alias='@type', serialization_alias='@type') # type: ignore
