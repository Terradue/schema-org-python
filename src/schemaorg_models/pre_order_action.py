from typing import Literal
from pydantic import Field
from schemaorg_models.trade_action import TradeAction


class PreOrderAction(TradeAction):
    """
An agent orders a (not yet released) object/product/service to be delivered/sent.
    """
    class_: Literal['https://schema.org/PreOrderAction'] = Field(default='https://schema.org/PreOrderAction', alias='@type', serialization_alias='@type') # type: ignore
