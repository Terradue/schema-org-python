from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class IncentiveType(Enumeration):
    """
The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies, etc.).
    """
    class_: Literal['https://schema.org/IncentiveType'] = Field( # type: ignore
        default='https://schema.org/IncentiveType',
        alias='@type',
        serialization_alias='@type'
    )
