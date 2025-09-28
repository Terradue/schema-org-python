from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class BroadcastFrequencySpecification(Intangible):
    """
The frequency in MHz and the modulation used for a particular BroadcastService.
    """
    class_: Literal['https://schema.org/BroadcastFrequencySpecification'] = Field( # type: ignore
        default='https://schema.org/BroadcastFrequencySpecification',
        alias='@type',
        serialization_alias='@type'
    )
    broadcastSubChannel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastSubChannel',
            'https://schema.org/broadcastSubChannel'
        ),
        serialization_alias='https://schema.org/broadcastSubChannel'
    )
    broadcastFrequencyValue: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequencyValue',
            'https://schema.org/broadcastFrequencyValue'
        ),
        serialization_alias='https://schema.org/broadcastFrequencyValue'
    )
    broadcastSignalModulation: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastSignalModulation',
            'https://schema.org/broadcastSignalModulation'
        ),
        serialization_alias='https://schema.org/broadcastSignalModulation'
    )
