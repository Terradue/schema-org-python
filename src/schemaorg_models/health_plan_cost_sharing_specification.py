from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

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

class HealthPlanCostSharingSpecification(Intangible):
    """
A description of costs to the patient under a given network or formulary.
    """
    class_: Literal['https://schema.org/HealthPlanCostSharingSpecification'] = Field( # type: ignore
        default='https://schema.org/HealthPlanCostSharingSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCoinsuranceRate',
            'https://schema.org/healthPlanCoinsuranceRate'
        ),
        serialization_alias='https://schema.org/healthPlanCoinsuranceRate'
    )
    healthPlanCopay: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCopay',
            'https://schema.org/healthPlanCopay'
        ),
        serialization_alias='https://schema.org/healthPlanCopay'
    )
    healthPlanCopayOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCopayOption',
            'https://schema.org/healthPlanCopayOption'
        ),
        serialization_alias='https://schema.org/healthPlanCopayOption'
    )
    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCoinsuranceOption',
            'https://schema.org/healthPlanCoinsuranceOption'
        ),
        serialization_alias='https://schema.org/healthPlanCoinsuranceOption'
    )
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanPharmacyCategory',
            'https://schema.org/healthPlanPharmacyCategory'
        ),
        serialization_alias='https://schema.org/healthPlanPharmacyCategory'
    )
