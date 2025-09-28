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
from .medical_entity import MedicalEntity
from .maximum_dose_schedule import MaximumDoseSchedule

class Substance(MedicalEntity):
    """
Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.
    """
    class_: Literal['https://schema.org/Substance'] = Field( # type: ignore
        default='https://schema.org/Substance',
        alias='@type',
        serialization_alias='@type'
    )
    maximumIntake: Optional[Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]] = Field(
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
