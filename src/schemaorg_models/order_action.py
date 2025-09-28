from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.trade_action import TradeAction

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
from schemaorg_models.delivery_method import DeliveryMethod

class OrderAction(TradeAction):
    """
An agent orders an object/product/service to be delivered/sent.
    """
    class_: Literal['https://schema.org/OrderAction'] = Field( # type: ignore
        default='https://schema.org/OrderAction',
        alias='@type',
        serialization_alias='@type'
    )
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryMethod',
            'https://schema.org/deliveryMethod'
        ),
        serialization_alias='https://schema.org/deliveryMethod'
    )
