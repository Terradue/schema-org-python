from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_procedure import MedicalProcedure

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
from schemaorg_models.medical_entity import MedicalEntity

class TherapeuticProcedure(MedicalProcedure):
    """
A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/TherapeuticProcedure'] = Field( # type: ignore
        default='https://schema.org/TherapeuticProcedure',
        alias='@type',
        serialization_alias='@type'
    )
    drug: Optional[Union["Drug", List["Drug"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drug',
            'https://schema.org/drug'
        ),
        serialization_alias='https://schema.org/drug'
    )
    adverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'adverseOutcome',
            'https://schema.org/adverseOutcome'
        ),
        serialization_alias='https://schema.org/adverseOutcome'
    )
    doseSchedule: Optional[Union["DoseSchedule", List["DoseSchedule"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseSchedule',
            'https://schema.org/doseSchedule'
        ),
        serialization_alias='https://schema.org/doseSchedule'
    )
