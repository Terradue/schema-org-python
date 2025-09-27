from typing import Literal
from pydantic import Field
from schemaorg_models.trade_action import TradeAction


class QuoteAction(TradeAction):
    """
An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
    class_: Literal['https://schema.org/QuoteAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
