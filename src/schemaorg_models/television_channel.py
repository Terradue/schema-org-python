from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.broadcast_channel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """
A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    """
    type_: Literal['https://schema.org/TelevisionChannel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TelevisionChannel'),serialization_alias='class') # type: ignore
