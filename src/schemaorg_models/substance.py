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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .maximum_dose_schedule import MaximumDoseSchedule

class Substance(MedicalEntity):
    '''
    Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.

    Attributes:
        maximumIntake: Recommended intake of this supplement for a given population as defined by a specific recommending authority.
        activeIngredient: An active ingredient, typically chemical compounds and/or biologic substances.
    '''
    class_: Literal['https://schema.org/Substance'] = Field( # type: ignore
        default='https://schema.org/Substance',
        alias='@type',
        serialization_alias='@type'
    )
    maximumIntake: Optional[Union['MaximumDoseSchedule', List['MaximumDoseSchedule']]] = Field(
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
