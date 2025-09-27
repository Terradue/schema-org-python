from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.financial_product import FinancialProduct

from schemaorg_models.monetary_amount import MonetaryAmount

class PaymentCard(FinancialProduct):
    """
A payment method using a credit, debit, store or other card to associate the payment with an account.
    """
    type_: Literal['https://schema.org/PaymentCard'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PaymentCard'),serialization_alias='class') # type: ignore
    monthlyMinimumRepaymentAmount: Optional[Union[float, List[float], MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('monthlyMinimumRepaymentAmount', 'https://schema.org/monthlyMinimumRepaymentAmount'),serialization_alias='https://schema.org/monthlyMinimumRepaymentAmount')
    floorLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('floorLimit', 'https://schema.org/floorLimit'),serialization_alias='https://schema.org/floorLimit')
    cashBack: Optional[Union[float, List[float], bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('cashBack', 'https://schema.org/cashBack'),serialization_alias='https://schema.org/cashBack')
    contactlessPayment: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('contactlessPayment', 'https://schema.org/contactlessPayment'),serialization_alias='https://schema.org/contactlessPayment')
