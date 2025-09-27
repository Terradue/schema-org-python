from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class HealthPlanNetwork(Intangible):
    """
A US-style health insurance plan network.
    """
    class_: Literal['https://schema.org/HealthPlanNetwork'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    healthPlanNetworkTier: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanNetworkTier', 'https://schema.org/healthPlanNetworkTier'), serialization_alias='https://schema.org/healthPlanNetworkTier')
    healthPlanNetworkId: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('healthPlanNetworkId', 'https://schema.org/healthPlanNetworkId'), serialization_alias='https://schema.org/healthPlanNetworkId')
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing'), serialization_alias='https://schema.org/healthPlanCostSharing')
