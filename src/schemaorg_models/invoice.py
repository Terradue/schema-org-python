from typing import Union, List, Optional
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.thing import Thing

class Invoice(Intangible):
    """
A statement of the money due for goods or services; a bill.
    """
    referencesOrder: Optional[Union["Order", List["Order"]]] = Field(default=None,validation_alias=AliasChoices('referencesOrder', 'https://schema.org/referencesOrder'),serialization_alias='https://schema.org/referencesOrder')
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('paymentDueDate', 'https://schema.org/paymentDueDate'),serialization_alias='https://schema.org/paymentDueDate')
    paymentDue: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('paymentDue', 'https://schema.org/paymentDue'),serialization_alias='https://schema.org/paymentDue')
    paymentMethodId: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('paymentMethodId', 'https://schema.org/paymentMethodId'),serialization_alias='https://schema.org/paymentMethodId')
    broker: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('broker', 'https://schema.org/broker'),serialization_alias='https://schema.org/broker')
    accountId: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('accountId', 'https://schema.org/accountId'),serialization_alias='https://schema.org/accountId')
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('category', 'https://schema.org/category'),serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    scheduledPaymentDate: Optional[Union[date, List[date]]] = Field(default=None,validation_alias=AliasChoices('scheduledPaymentDate', 'https://schema.org/scheduledPaymentDate'),serialization_alias='https://schema.org/scheduledPaymentDate')
    totalPaymentDue: Optional[Union["PriceSpecification", List["PriceSpecification"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None,validation_alias=AliasChoices('totalPaymentDue', 'https://schema.org/totalPaymentDue'),serialization_alias='https://schema.org/totalPaymentDue')
    customer: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('customer', 'https://schema.org/customer'),serialization_alias='https://schema.org/customer')
    paymentMethod: Optional[Union[str, List[str], "PaymentMethod", List["PaymentMethod"]]] = Field(default=None,validation_alias=AliasChoices('paymentMethod', 'https://schema.org/paymentMethod'),serialization_alias='https://schema.org/paymentMethod')
    minimumPaymentDue: Optional[Union["PriceSpecification", List["PriceSpecification"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None,validation_alias=AliasChoices('minimumPaymentDue', 'https://schema.org/minimumPaymentDue'),serialization_alias='https://schema.org/minimumPaymentDue')
    confirmationNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('confirmationNumber', 'https://schema.org/confirmationNumber'),serialization_alias='https://schema.org/confirmationNumber')
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('provider', 'https://schema.org/provider'),serialization_alias='https://schema.org/provider')
    paymentStatus: Optional[Union[str, List[str], "PaymentStatusType", List["PaymentStatusType"]]] = Field(default=None,validation_alias=AliasChoices('paymentStatus', 'https://schema.org/paymentStatus'),serialization_alias='https://schema.org/paymentStatus')
    billingPeriod: Optional[Union["Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('billingPeriod', 'https://schema.org/billingPeriod'),serialization_alias='https://schema.org/billingPeriod')
