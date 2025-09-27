from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.broadcast_channel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """
A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
    type_: Literal['https://schema.org/RadioChannel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioChannel'),serialization_alias='class') # type: ignore
