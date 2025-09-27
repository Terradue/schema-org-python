from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.medical_entity import MedicalEntity

class MedicalProcedure(MedicalEntity):
    """
A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.
    """
    class_: Literal['https://schema.org/MedicalProcedure'] = Field(default='https://schema.org/MedicalProcedure', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    bodyLocation: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('bodyLocation', 'https://schema.org/bodyLocation'), serialization_alias='https://schema.org/bodyLocation')
    preparation: Optional[Union[MedicalEntity, List[MedicalEntity], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('preparation', 'https://schema.org/preparation'), serialization_alias='https://schema.org/preparation')
    status: Optional[Union["EventStatusType", List["EventStatusType"], "MedicalStudyStatus", List["MedicalStudyStatus"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('status', 'https://schema.org/status'), serialization_alias='https://schema.org/status')
    howPerformed: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('howPerformed', 'https://schema.org/howPerformed'), serialization_alias='https://schema.org/howPerformed')
    procedureType: Optional[Union["MedicalProcedureType", List["MedicalProcedureType"]]] = Field(default=None, validation_alias=AliasChoices('procedureType', 'https://schema.org/procedureType'), serialization_alias='https://schema.org/procedureType')
    followup: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('followup', 'https://schema.org/followup'), serialization_alias='https://schema.org/followup')
