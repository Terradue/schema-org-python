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
from .local_business import LocalBusiness

class FinancialService(LocalBusiness):
    '''
    Financial services business.

    Attributes:
        feesAndCommissionsSpecification: Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    '''
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
