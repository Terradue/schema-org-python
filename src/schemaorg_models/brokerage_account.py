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
from .investment_or_deposit import InvestmentOrDeposit

class BrokerageAccount(InvestmentOrDeposit):
    '''
    An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.
    '''
    class_: Literal['https://schema.org/BrokerageAccount'] = Field( # type: ignore
        default='https://schema.org/BrokerageAccount',
        alias='@type',
        serialization_alias='@type'
    )
