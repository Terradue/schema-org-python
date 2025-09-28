from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.trade_action import TradeAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class QuoteAction(TradeAction):
    """
An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
    class_: Literal['https://schema.org/QuoteAction'] = Field( # type: ignore
        default='https://schema.org/QuoteAction',
        alias='@type',
        serialization_alias='@type'
    )
