from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction


class QuoteAction(TradeAction):
    """
An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
    type_: Literal['https://schema.org/QuoteAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/QuoteAction'),serialization_alias='class') # type: ignore
