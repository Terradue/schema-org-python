from typing import Literal
from pydantic import Field
from schemaorg_models.broadcast_channel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """
A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/RadioChannel'] = Field(default='https://schema.org/RadioChannel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
