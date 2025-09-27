from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.defined_region import DefinedRegion

class DeliveryTimeSettings(StructuredValue):
    """
A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].
    """
    type_: Literal['https://schema.org/DeliveryTimeSettings'] = Field(default='https://schema.org/DeliveryTimeSettings', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    transitTimeLabel: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('transitTimeLabel', 'https://schema.org/transitTimeLabel'), serialization_alias='https://schema.org/transitTimeLabel')
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('isUnlabelledFallback', 'https://schema.org/isUnlabelledFallback'), serialization_alias='https://schema.org/isUnlabelledFallback')
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(default=None, validation_alias=AliasChoices('shippingDestination', 'https://schema.org/shippingDestination'), serialization_alias='https://schema.org/shippingDestination')
    deliveryTime: Optional[Union["ShippingDeliveryTime", List["ShippingDeliveryTime"]]] = Field(default=None, validation_alias=AliasChoices('deliveryTime', 'https://schema.org/deliveryTime'), serialization_alias='https://schema.org/deliveryTime')
