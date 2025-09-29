from __future__ import annotations
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
from .substance import Substance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_enumeration import MedicalEnumeration
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .drug_legal_status import DrugLegalStatus
    from .recommended_dose_schedule import RecommendedDoseSchedule

class DietarySupplement(Substance):
    """
A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.
    """
    class_: Literal['https://schema.org/DietarySupplement'] = Field( # type: ignore
        default='https://schema.org/DietarySupplement',
        alias='@type',
        serialization_alias='@type'
    )
    proprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proprietaryName',
            'https://schema.org/proprietaryName'
        ),
        serialization_alias='https://schema.org/proprietaryName'
    )
    mechanismOfAction: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mechanismOfAction',
            'https://schema.org/mechanismOfAction'
        ),
        serialization_alias='https://schema.org/mechanismOfAction'
    )
    isProprietary: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isProprietary',
            'https://schema.org/isProprietary'
        ),
        serialization_alias='https://schema.org/isProprietary'
    )
    maximumIntake: Optional[Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake',
            'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake'
    )
    activeIngredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient',
            'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient'
    )
    recommendedIntake: Optional[Union["RecommendedDoseSchedule", List["RecommendedDoseSchedule"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recommendedIntake',
            'https://schema.org/recommendedIntake'
        ),
        serialization_alias='https://schema.org/recommendedIntake'
    )
    safetyConsideration: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'safetyConsideration',
            'https://schema.org/safetyConsideration'
        ),
        serialization_alias='https://schema.org/safetyConsideration'
    )
    targetPopulation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetPopulation',
            'https://schema.org/targetPopulation'
        ),
        serialization_alias='https://schema.org/targetPopulation'
    )
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"], "MedicalEnumeration", List["MedicalEnumeration"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalStatus',
            'https://schema.org/legalStatus'
        ),
        serialization_alias='https://schema.org/legalStatus'
    )
    nonProprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonProprietaryName',
            'https://schema.org/nonProprietaryName'
        ),
        serialization_alias='https://schema.org/nonProprietaryName'
    )
