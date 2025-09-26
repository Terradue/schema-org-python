from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction

from schemaorg_models.delivery_method import DeliveryMethod

class OrderAction(TradeAction):
    """
An agent orders an object/product/service to be delivered/sent.
    """
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None,validation_alias=AliasChoices('deliveryMethod', 'https://schema.org/deliveryMethod'),serialization_alias='https://schema.org/deliveryMethod')
