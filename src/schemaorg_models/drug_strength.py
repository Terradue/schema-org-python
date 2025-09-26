from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible

from schemaorg_models.administrative_area import AdministrativeArea

class DrugStrength(MedicalIntangible):
    """
A specific strength in which a medical drug is available in a specific country.
    """
    strengthUnit: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('strengthUnit', 'https://schema.org/strengthUnit'),serialization_alias='https://schema.org/strengthUnit')
    maximumIntake: Optional[Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]] = Field(default=None,validation_alias=AliasChoices('maximumIntake', 'https://schema.org/maximumIntake'),serialization_alias='https://schema.org/maximumIntake')
    availableIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(default=None,validation_alias=AliasChoices('availableIn', 'https://schema.org/availableIn'),serialization_alias='https://schema.org/availableIn')
    strengthValue: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('strengthValue', 'https://schema.org/strengthValue'),serialization_alias='https://schema.org/strengthValue')
    activeIngredient: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('activeIngredient', 'https://schema.org/activeIngredient'),serialization_alias='https://schema.org/activeIngredient')
