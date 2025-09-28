from __future__ import annotations

from .trade_action import TradeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PreOrderAction(TradeAction):
    """
An agent orders a (not yet released) object/product/service to be delivered/sent.
    """
    class_: Literal['https://schema.org/PreOrderAction'] = Field( # type: ignore
        default='https://schema.org/PreOrderAction',
        alias='@type',
        serialization_alias='@type'
    )
