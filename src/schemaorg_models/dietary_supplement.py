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
from .substance import Substance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_enumeration import MedicalEnumeration
    from .recommended_dose_schedule import RecommendedDoseSchedule
    from .drug_legal_status import DrugLegalStatus
    from .maximum_dose_schedule import MaximumDoseSchedule

class DietarySupplement(Substance):
    '''
    A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.

    Attributes:
        proprietaryName: Proprietary name given to the diet plan, typically by its originator or creator.
        mechanismOfAction: The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.
        isProprietary: True if this item's name is a proprietary/brand name (vs. generic name).
        maximumIntake: Recommended intake of this supplement for a given population as defined by a specific recommending authority.
        activeIngredient: An active ingredient, typically chemical compounds and/or biologic substances.
        recommendedIntake: Recommended intake of this supplement for a given population as defined by a specific recommending authority.
        safetyConsideration: Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.
        targetPopulation: Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.
        legalStatus: The drug or supplement's legal status, including any controlled substance schedules that apply.
        nonProprietaryName: The generic name of this drug or supplement.
    '''
    class_: Literal['https://schema.org/DietarySupplement'] = Field( # type: ignore
        default='https://schema.org/DietarySupplement',
        alias='@type',
        serialization_alias='@type'
    )
    proprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    mechanismOfAction: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isProprietary: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumIntake: Optional[Union['MaximumDoseSchedule', List['MaximumDoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    activeIngredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    recommendedIntake: Optional[Union['RecommendedDoseSchedule', List['RecommendedDoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    safetyConsideration: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    targetPopulation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    legalStatus: Optional[Union['DrugLegalStatus', List['DrugLegalStatus'], 'MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    nonProprietaryName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
