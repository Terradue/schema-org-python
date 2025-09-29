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
from .medical_procedure import MedicalProcedure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug import Drug
    from .medical_entity import MedicalEntity
    from .dose_schedule import DoseSchedule

class TherapeuticProcedure(MedicalProcedure):
    '''
    A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

    Attributes:
        drug: Specifying a drug or medicine used in a medication procedure.
        adverseOutcome: A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
        doseSchedule: A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
    '''
    class_: Literal['https://schema.org/TherapeuticProcedure'] = Field( # type: ignore
        default='https://schema.org/TherapeuticProcedure',
        alias='@type',
        serialization_alias='@type'
    )
    drug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    adverseOutcome: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    doseSchedule: Optional[Union['DoseSchedule', List['DoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
