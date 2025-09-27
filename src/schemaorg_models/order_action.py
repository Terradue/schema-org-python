from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction

from schemaorg_models.delivery_method import DeliveryMethod

class OrderAction(TradeAction):
    """
An agent orders an object/product/service to be delivered/sent.
    """
    class_: Literal['https://schema.org/OrderAction'] = Field(default='https://schema.org/OrderAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None, validation_alias=AliasChoices('deliveryMethod', 'https://schema.org/deliveryMethod'), serialization_alias='https://schema.org/deliveryMethod')
