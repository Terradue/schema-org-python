from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction


class PreOrderAction(TradeAction):
    """
An agent orders a (not yet released) object/product/service to be delivered/sent.
    """
    type_: Literal['https://schema.org/PreOrderAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PreOrderAction'),serialization_alias='class') # type: ignore
