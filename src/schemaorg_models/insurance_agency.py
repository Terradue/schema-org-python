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
from .financial_service import FinancialService

class InsuranceAgency(FinancialService):
    '''
    An Insurance agency.
    '''
    class_: Literal['https://schema.org/InsuranceAgency'] = Field( # type: ignore
        default='https://schema.org/InsuranceAgency',
        alias='@type',
        serialization_alias='@type'
    )
