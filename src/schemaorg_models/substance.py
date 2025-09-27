from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class Substance(MedicalEntity):
    """
Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.
    """
    type_: Literal['https://schema.org/Substance'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Substance'),serialization_alias='class') # type: ignore
    maximumIntake: Optional[Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]] = Field(default=None,validation_alias=AliasChoices('maximumIntake', 'https://schema.org/maximumIntake'),serialization_alias='https://schema.org/maximumIntake')
    activeIngredient: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('activeIngredient', 'https://schema.org/activeIngredient'),serialization_alias='https://schema.org/activeIngredient')
