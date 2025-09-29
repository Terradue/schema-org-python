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

class HealthPlanNetwork(Intangible):
    '''
    A US-style health insurance plan network.

    Attributes:
        healthPlanNetworkTier: The tier(s) for this network.
        healthPlanNetworkId: Name or unique ID of network. (Networks are often reused across different insurance plans.)
        healthPlanCostSharing: The costs to the patient for services under this network or formulary.
    '''
    class_: Literal['https://schema.org/HealthPlanNetwork'] = Field( # type: ignore
        default='https://schema.org/HealthPlanNetwork',
        alias='@type',
        serialization_alias='@type'
    )
    healthPlanNetworkTier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanNetworkTier',
            'https://schema.org/healthPlanNetworkTier'
        ),
        serialization_alias='https://schema.org/healthPlanNetworkTier'
    )
    healthPlanNetworkId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanNetworkId',
            'https://schema.org/healthPlanNetworkId'
        ),
        serialization_alias='https://schema.org/healthPlanNetworkId'
    )
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCostSharing',
            'https://schema.org/healthPlanCostSharing'
        ),
        serialization_alias='https://schema.org/healthPlanCostSharing'
    )
