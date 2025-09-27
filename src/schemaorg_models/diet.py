from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.lifestyle_modification import LifestyleModification

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class Diet(LifestyleModification):
    """
A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.
    """
    type_: Literal['https://schema.org/Diet'] = Field(default='https://schema.org/Diet', alias='@type', serialization_alias='@type') # type: ignore
    risks: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('risks', 'https://schema.org/risks'), serialization_alias='https://schema.org/risks')
    physiologicalBenefits: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('physiologicalBenefits', 'https://schema.org/physiologicalBenefits'), serialization_alias='https://schema.org/physiologicalBenefits')
    dietFeatures: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('dietFeatures', 'https://schema.org/dietFeatures'), serialization_alias='https://schema.org/dietFeatures')
    expertConsiderations: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('expertConsiderations', 'https://schema.org/expertConsiderations'), serialization_alias='https://schema.org/expertConsiderations')
    endorsers: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('endorsers', 'https://schema.org/endorsers'), serialization_alias='https://schema.org/endorsers')
