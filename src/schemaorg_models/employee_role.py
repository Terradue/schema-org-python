from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.organization_role import OrganizationRole

from schemaorg_models.price_specification import PriceSpecification
from schemaorg_models.monetary_amount import MonetaryAmount

class EmployeeRole(OrganizationRole):
    """
A subclass of OrganizationRole used to describe employee relationships.
    """
    salaryCurrency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('salaryCurrency', 'https://schema.org/salaryCurrency'),serialization_alias='https://schema.org/salaryCurrency')
    baseSalary: Optional[Union[float, List[float], PriceSpecification, List[PriceSpecification], MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('baseSalary', 'https://schema.org/baseSalary'),serialization_alias='https://schema.org/baseSalary')
