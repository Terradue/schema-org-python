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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .price_specification import PriceSpecification

class HealthPlanCostSharingSpecification(Intangible):
    '''
    A description of costs to the patient under a given network or formulary.

    Attributes:
        healthPlanCoinsuranceRate: The rate of coinsurance expressed as a number between 0.0 and 1.0.
        healthPlanCopay: The copay amount.
        healthPlanCopayOption: Whether the copay is before or after deductible, etc. TODO: Is this a closed set?
        healthPlanCoinsuranceOption: Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed set?
        healthPlanPharmacyCategory: The category or type of pharmacy associated with this cost sharing.
    '''
    class_: Literal['https://schema.org/HealthPlanCostSharingSpecification'] = Field( # type: ignore
        default='https://schema.org/HealthPlanCostSharingSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    healthPlanCoinsuranceRate: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanCopay: Optional[Union['PriceSpecification', List['PriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanCopayOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanCoinsuranceOption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthPlanPharmacyCategory: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
