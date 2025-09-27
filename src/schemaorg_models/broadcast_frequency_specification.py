from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class BroadcastFrequencySpecification(Intangible):
    """
The frequency in MHz and the modulation used for a particular BroadcastService.
    """
    type_: Literal['https://schema.org/BroadcastFrequencySpecification'] = Field(default='https://schema.org/BroadcastFrequencySpecification', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    broadcastSubChannel: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('broadcastSubChannel', 'https://schema.org/broadcastSubChannel'), serialization_alias='https://schema.org/broadcastSubChannel')
    broadcastFrequencyValue: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('broadcastFrequencyValue', 'https://schema.org/broadcastFrequencyValue'), serialization_alias='https://schema.org/broadcastFrequencyValue')
    broadcastSignalModulation: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('broadcastSignalModulation', 'https://schema.org/broadcastSignalModulation'), serialization_alias='https://schema.org/broadcastSignalModulation')
