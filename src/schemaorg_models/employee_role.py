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
from .organization_role import OrganizationRole
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification

class EmployeeRole(OrganizationRole):
    '''
    A subclass of OrganizationRole used to describe employee relationships.

    Attributes:
        salaryCurrency: The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.
        baseSalary: The base salary of the job or of an employee in an EmployeeRole.
    '''
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
    baseSalary: Optional[Union[float, List[float], 'PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'baseSalary',
            'https://schema.org/baseSalary'
        ),
        serialization_alias='https://schema.org/baseSalary'
    )
