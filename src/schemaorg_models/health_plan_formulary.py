from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class HealthPlanFormulary(Intangible):
    """
For a given health insurance plan, the specification for costs and coverage of prescription drugs.
    """
    class_: Literal['https://schema.org/HealthPlanFormulary'] = Field(default='https://schema.org/HealthPlanFormulary', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    offersPrescriptionByMail: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('offersPrescriptionByMail', 'https://schema.org/offersPrescriptionByMail'), serialization_alias='https://schema.org/offersPrescriptionByMail')
    healthPlanDrugTier: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'), serialization_alias='https://schema.org/healthPlanDrugTier')
    healthPlanCostSharing: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing'), serialization_alias='https://schema.org/healthPlanCostSharing')
