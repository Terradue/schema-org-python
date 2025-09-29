from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .trade_action import TradeAction

class PreOrderAction(TradeAction):
    '''
    An agent orders a (not yet released) object/product/service to be delivered/sent.
    '''
    class_: Literal['https://schema.org/PreOrderAction'] = Field( # type: ignore
        default='https://schema.org/PreOrderAction',
        alias='@type',
        serialization_alias='@type'
    )
