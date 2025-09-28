from __future__ import annotations
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
from .monetary_amount import MonetaryAmount
from .price_specification import PriceSpecification
from .organization_role import OrganizationRole

class EmployeeRole(OrganizationRole):
    """
A subclass of OrganizationRole used to describe employee relationships.
    """
    class_: Literal['https://schema.org/EmployeeRole'] = Field( # type: ignore
        default='https://schema.org/EmployeeRole',
        alias='@type',
        serialization_alias='@type'
    )
    salaryCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'salaryCurrency',
            'https://schema.org/salaryCurrency'
        ),
        serialization_alias='https://schema.org/salaryCurrency'
    )
    baseSalary: Optional[Union[float, List[float], PriceSpecification, List[PriceSpecification], MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'baseSalary',
            'https://schema.org/baseSalary'
        ),
        serialization_alias='https://schema.org/baseSalary'
    )
