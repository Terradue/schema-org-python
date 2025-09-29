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

class InvestmentFund(InvestmentOrDeposit):
    '''
    A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.
    '''
    class_: Literal['https://schema.org/InvestmentFund'] = Field( # type: ignore
        default='https://schema.org/InvestmentFund',
        alias='@type',
        serialization_alias='@type'
    )
