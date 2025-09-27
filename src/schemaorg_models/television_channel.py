from typing import Literal
from pydantic import Field
from schemaorg_models.broadcast_channel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """
A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/TelevisionChannel'] = Field('class', alias='class', serialization_alias='class') # type: ignore
