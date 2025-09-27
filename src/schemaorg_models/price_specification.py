from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.member_program_tier import MemberProgramTier

class PriceSpecification(StructuredValue):
    """
One or more detailed price specifications, indicating the unit price and delivery or payment charges.
    """
    type_: Literal['https://schema.org/PriceSpecification'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PriceSpecification'),serialization_alias='class') # type: ignore
    minPrice: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('minPrice', 'https://schema.org/minPrice'),serialization_alias='https://schema.org/minPrice')
    maxPrice: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('maxPrice', 'https://schema.org/maxPrice'),serialization_alias='https://schema.org/maxPrice')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'),serialization_alias='https://schema.org/priceCurrency')
    valueAddedTaxIncluded: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('valueAddedTaxIncluded', 'https://schema.org/valueAddedTaxIncluded'),serialization_alias='https://schema.org/valueAddedTaxIncluded')
    eligibleQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('eligibleQuantity', 'https://schema.org/eligibleQuantity'),serialization_alias='https://schema.org/eligibleQuantity')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'),serialization_alias='https://schema.org/validThrough')
    eligibleTransactionVolume: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume'),serialization_alias='https://schema.org/eligibleTransactionVolume')
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),serialization_alias='https://schema.org/validFrom')
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None,validation_alias=AliasChoices('validForMemberTier', 'https://schema.org/validForMemberTier'),serialization_alias='https://schema.org/validForMemberTier')
    membershipPointsEarned: Optional[Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('membershipPointsEarned', 'https://schema.org/membershipPointsEarned'),serialization_alias='https://schema.org/membershipPointsEarned')
    price: Optional[Union[str, List[str], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('price', 'https://schema.org/price'),serialization_alias='https://schema.org/price')
