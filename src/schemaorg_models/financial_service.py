from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .local_business import LocalBusiness

class FinancialService(LocalBusiness):
    """
Financial services business.
    """
    class_: Literal['https://schema.org/FinancialService'] = Field( # type: ignore
        default='https://schema.org/FinancialService',
        alias='@type',
        serialization_alias='@type'
    )
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'feesAndCommissionsSpecification',
            'https://schema.org/feesAndCommissionsSpecification'
        ),
        serialization_alias='https://schema.org/feesAndCommissionsSpecification'
    )
