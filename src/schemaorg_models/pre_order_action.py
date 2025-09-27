from typing import Literal
from pydantic import Field
from schemaorg_models.trade_action import TradeAction


class PreOrderAction(TradeAction):
    """
An agent orders a (not yet released) object/product/service to be delivered/sent.
    """
    type_: Literal['https://schema.org/PreOrderAction'] = Field(default='https://schema.org/PreOrderAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
