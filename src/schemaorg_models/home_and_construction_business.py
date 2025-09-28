from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HomeAndConstructionBusiness(LocalBusiness):
    """
A construction business.\
\
A HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    """
    class_: Literal['https://schema.org/HomeAndConstructionBusiness'] = Field( # type: ignore
        default='https://schema.org/HomeAndConstructionBusiness',
        alias='@type',
        serialization_alias='@type'
    )
