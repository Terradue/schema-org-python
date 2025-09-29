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
from .medical_intangible import MedicalIntangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .maximum_dose_schedule import MaximumDoseSchedule

class DrugStrength(MedicalIntangible):
    '''
    A specific strength in which a medical drug is available in a specific country.

    Attributes:
        strengthUnit: The units of an active ingredient's strength, e.g. mg.
        maximumIntake: Recommended intake of this supplement for a given population as defined by a specific recommending authority.
        availableIn: The location in which the strength is available.
        strengthValue: The value of an active ingredient's strength, e.g. 325.
        activeIngredient: An active ingredient, typically chemical compounds and/or biologic substances.
    '''
    class_: Literal['https://schema.org/DrugStrength'] = Field( # type: ignore
        default='https://schema.org/DrugStrength',
        alias='@type',
        serialization_alias='@type'
    )
    strengthUnit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'strengthUnit',
            'https://schema.org/strengthUnit'
        ),
        serialization_alias='https://schema.org/strengthUnit'
    )
    maximumIntake: Optional[Union['MaximumDoseSchedule', List['MaximumDoseSchedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake',
            'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake'
    )
    availableIn: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableIn',
            'https://schema.org/availableIn'
        ),
        serialization_alias='https://schema.org/availableIn'
    )
    strengthValue: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'strengthValue',
            'https://schema.org/strengthValue'
        ),
        serialization_alias='https://schema.org/strengthValue'
    )
    activeIngredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient',
            'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient'
    )
