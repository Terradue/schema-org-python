from typing import Union, List, Optional
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.product import Product
from schemaorg_models.administrative_area import AdministrativeArea
from schemaorg_models.place import Place

class FinancialIncentive(Intangible):
    """
<p>Represents financial incentives for goods/services offered by an organization (or individual).</p>

<p>Typically contains the [[name]] of the incentive, the [[incentivizedItem]], the [[incentiveAmount]], the [[incentiveStatus]], [[incentiveType]], the [[provider]] of the incentive, and [[eligibleWithSupplier]].</p>

<p>Optionally contains criteria on whether the incentive is limited based on [[purchaseType]], [[purchasePriceLimit]], [[incomeLimit]], and the [[qualifiedExpense]].
    
    """
    incomeLimit: Optional[Union[str, List[str], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None,validation_alias=AliasChoices('incomeLimit', 'https://schema.org/incomeLimit'),serialization_alias='https://schema.org/incomeLimit')
    qualifiedExpense: Optional[Union["IncentiveQualifiedExpenseType", List["IncentiveQualifiedExpenseType"]]] = Field(default=None,validation_alias=AliasChoices('qualifiedExpense', 'https://schema.org/qualifiedExpense'),serialization_alias='https://schema.org/qualifiedExpense')
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('provider', 'https://schema.org/provider'),serialization_alias='https://schema.org/provider')
    incentivizedItem: Optional[Union[DefinedTerm, List[DefinedTerm], Product, List[Product]]] = Field(default=None,validation_alias=AliasChoices('incentivizedItem', 'https://schema.org/incentivizedItem'),serialization_alias='https://schema.org/incentivizedItem')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'),serialization_alias='https://schema.org/validThrough')
    areaServed: Optional[Union["GeoShape", List["GeoShape"], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),serialization_alias='https://schema.org/areaServed')
    publisher: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('publisher', 'https://schema.org/publisher'),serialization_alias='https://schema.org/publisher')
    eligibleWithSupplier: Optional[Union[Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('eligibleWithSupplier', 'https://schema.org/eligibleWithSupplier'),serialization_alias='https://schema.org/eligibleWithSupplier')
    purchaseType: Optional[Union["PurchaseType", List["PurchaseType"]]] = Field(default=None,validation_alias=AliasChoices('purchaseType', 'https://schema.org/purchaseType'),serialization_alias='https://schema.org/purchaseType')
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),serialization_alias='https://schema.org/validFrom')
    incentiveAmount: Optional[Union["UnitPriceSpecification", List["UnitPriceSpecification"], "QuantitativeValue", List["QuantitativeValue"], "LoanOrCredit", List["LoanOrCredit"]]] = Field(default=None,validation_alias=AliasChoices('incentiveAmount', 'https://schema.org/incentiveAmount'),serialization_alias='https://schema.org/incentiveAmount')
    purchasePriceLimit: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None,validation_alias=AliasChoices('purchasePriceLimit', 'https://schema.org/purchasePriceLimit'),serialization_alias='https://schema.org/purchasePriceLimit')
    incentiveType: Optional[Union["IncentiveType", List["IncentiveType"]]] = Field(default=None,validation_alias=AliasChoices('incentiveType', 'https://schema.org/incentiveType'),serialization_alias='https://schema.org/incentiveType')
    incentiveStatus: Optional[Union["IncentiveStatus", List["IncentiveStatus"]]] = Field(default=None,validation_alias=AliasChoices('incentiveStatus', 'https://schema.org/incentiveStatus'),serialization_alias='https://schema.org/incentiveStatus')
