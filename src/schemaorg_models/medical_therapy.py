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
from .therapeutic_procedure import TherapeuticProcedure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_contraindication import MedicalContraindication
    from .medical_entity import MedicalEntity

class MedicalTherapy(TherapeuticProcedure):
    '''
    Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.

    Attributes:
        seriousAdverseOutcome: A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        contraindication: A contraindication for this therapy.
        duplicateTherapy: A therapy that duplicates or overlaps this one.
    '''
    class_: Literal['https://schema.org/MedicalTherapy'] = Field( # type: ignore
        default='https://schema.org/MedicalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
    seriousAdverseOutcome: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    contraindication: Optional[Union[str, List[str], 'MedicalContraindication', List['MedicalContraindication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    duplicateTherapy: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
