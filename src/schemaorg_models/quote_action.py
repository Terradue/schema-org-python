from typing import Literal
from pydantic import Field
from schemaorg_models.trade_action import TradeAction


class QuoteAction(TradeAction):
    """
An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
    type_: Literal['https://schema.org/QuoteAction'] = Field(default='https://schema.org/QuoteAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
