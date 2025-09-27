from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    """
A description of costs to the patient under a given network or formulary.
    """
    type_: Literal['https://schema.org/HealthPlanCostSharingSpecification'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HealthPlanCostSharingSpecification'),serialization_alias='class') # type: ignore
    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('healthPlanCoinsuranceRate', 'https://schema.org/healthPlanCoinsuranceRate'),serialization_alias='https://schema.org/healthPlanCoinsuranceRate')
    healthPlanCopay: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('healthPlanCopay', 'https://schema.org/healthPlanCopay'),serialization_alias='https://schema.org/healthPlanCopay')
    healthPlanCopayOption: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanCopayOption', 'https://schema.org/healthPlanCopayOption'),serialization_alias='https://schema.org/healthPlanCopayOption')
    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanCoinsuranceOption', 'https://schema.org/healthPlanCoinsuranceOption'),serialization_alias='https://schema.org/healthPlanCoinsuranceOption')
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanPharmacyCategory', 'https://schema.org/healthPlanPharmacyCategory'),serialization_alias='https://schema.org/healthPlanPharmacyCategory')
