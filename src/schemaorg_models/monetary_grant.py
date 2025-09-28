from __future__ import annotations

from .grant import Grant    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.monetary_amount import MonetaryAmount
from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class MonetaryGrant(Grant):
    """
A monetary grant.
    """
    class_: Literal['https://schema.org/MonetaryGrant'] = Field( # type: ignore
        default='https://schema.org/MonetaryGrant',
        alias='@type',
        serialization_alias='@type'
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amount',
            'https://schema.org/amount'
        ),
        serialization_alias='https://schema.org/amount'
    )
    funder: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
