from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.broadcast_frequency_specification import BroadcastFrequencySpecification

class BroadcastChannel(Intangible):
    """
A unique instance of a BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/BroadcastChannel'] = Field(default='https://schema.org/BroadcastChannel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    inBroadcastLineup: Optional[Union["CableOrSatelliteService", List["CableOrSatelliteService"]]] = Field(default=None, validation_alias=AliasChoices('inBroadcastLineup', 'https://schema.org/inBroadcastLineup'), serialization_alias='https://schema.org/inBroadcastLineup')
    broadcastChannelId: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('broadcastChannelId', 'https://schema.org/broadcastChannelId'), serialization_alias='https://schema.org/broadcastChannelId')
    providesBroadcastService: Optional[Union["BroadcastService", List["BroadcastService"]]] = Field(default=None, validation_alias=AliasChoices('providesBroadcastService', 'https://schema.org/providesBroadcastService'), serialization_alias='https://schema.org/providesBroadcastService')
    broadcastFrequency: Optional[Union[str, List[str], BroadcastFrequencySpecification, List[BroadcastFrequencySpecification]]] = Field(default=None, validation_alias=AliasChoices('broadcastFrequency', 'https://schema.org/broadcastFrequency'), serialization_alias='https://schema.org/broadcastFrequency')
    broadcastServiceTier: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('broadcastServiceTier', 'https://schema.org/broadcastServiceTier'), serialization_alias='https://schema.org/broadcastServiceTier')
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('genre', 'https://schema.org/genre'), serialization_alias='https://schema.org/genre')
    @field_serializer('genre')
    def genre2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

