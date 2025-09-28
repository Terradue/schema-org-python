from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class LegalService(LocalBusiness):
    """
A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    """
    class_: Literal['https://schema.org/LegalService'] = Field( # type: ignore
        default='https://schema.org/LegalService',
        alias='@type',
        serialization_alias='@type'
    )
