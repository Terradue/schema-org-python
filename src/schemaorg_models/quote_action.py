from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .trade_action import TradeAction

class QuoteAction(TradeAction):
    """
An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
    class_: Literal['https://schema.org/QuoteAction'] = Field( # type: ignore
        default='https://schema.org/QuoteAction',
        alias='@type',
        serialization_alias='@type'
    )
