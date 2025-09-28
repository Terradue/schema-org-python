from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

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
