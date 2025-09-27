from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class HealthPlanFormulary(Intangible):
    """
For a given health insurance plan, the specification for costs and coverage of prescription drugs.
    """
    type_: Literal['https://schema.org/HealthPlanFormulary'] = Field(default='https://schema.org/HealthPlanFormulary', alias='@type', serialization_alias='@type') # type: ignore
    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('offersPrescriptionByMail', 'https://schema.org/offersPrescriptionByMail'), serialization_alias='https://schema.org/offersPrescriptionByMail')
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'), serialization_alias='https://schema.org/healthPlanDrugTier')
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing'), serialization_alias='https://schema.org/healthPlanCostSharing')
