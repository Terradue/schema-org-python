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
from .therapeutic_procedure import TherapeuticProcedure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_entity import MedicalEntity
    from .medical_contraindication import MedicalContraindication

class MedicalTherapy(TherapeuticProcedure):
    """
Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.
    """
    class_: Literal['https://schema.org/MedicalTherapy'] = Field( # type: ignore
        default='https://schema.org/MedicalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
    seriousAdverseOutcome: Optional[Union["MedicalEntity", List["MedicalEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seriousAdverseOutcome',
            'https://schema.org/seriousAdverseOutcome'
        ),
        serialization_alias='https://schema.org/seriousAdverseOutcome'
    )
    contraindication: Optional[Union[str, List[str], "MedicalContraindication", List["MedicalContraindication"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contraindication',
            'https://schema.org/contraindication'
        ),
        serialization_alias='https://schema.org/contraindication'
    )
    duplicateTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duplicateTherapy',
            'https://schema.org/duplicateTherapy'
        ),
        serialization_alias='https://schema.org/duplicateTherapy'
    )
