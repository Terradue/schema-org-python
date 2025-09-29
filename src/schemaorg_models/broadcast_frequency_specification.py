from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue
    from .quantitative_value import QuantitativeValue

class BroadcastFrequencySpecification(Intangible):
    '''
    The frequency in MHz and the modulation used for a particular BroadcastService.

    Attributes:
        broadcastSubChannel: The subchannel used for the broadcast.
        broadcastFrequencyValue: The frequency in MHz for a particular broadcast.
        broadcastSignalModulation: The modulation (e.g. FM, AM, etc) used by a particular broadcast service.
    '''
    class_: Literal['https://schema.org/BroadcastFrequencySpecification'] = Field( # type: ignore
        default='https://schema.org/BroadcastFrequencySpecification',
        alias='@type',
        serialization_alias='@type'
    )
    broadcastSubChannel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastFrequencyValue: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    broadcastSignalModulation: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
