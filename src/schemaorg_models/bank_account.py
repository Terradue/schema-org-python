from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.financial_product import FinancialProduct

from schemaorg_models.monetary_amount import MonetaryAmount

class BankAccount(FinancialProduct):
    """
A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.
    """
    bankAccountType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('bankAccountType', 'https://schema.org/bankAccountType'),serialization_alias='https://schema.org/bankAccountType')
    @field_serializer('bankAccountType')
    def bankAccountType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    accountOverdraftLimit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('accountOverdraftLimit', 'https://schema.org/accountOverdraftLimit'),serialization_alias='https://schema.org/accountOverdraftLimit')
    accountMinimumInflow: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('accountMinimumInflow', 'https://schema.org/accountMinimumInflow'),serialization_alias='https://schema.org/accountMinimumInflow')
