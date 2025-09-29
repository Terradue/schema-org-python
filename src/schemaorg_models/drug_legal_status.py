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

class DrugLegalStatus(MedicalIntangible):
    '''
    The legal availability status of a medical drug.

    Attributes:
        applicableLocation: The location in which the status applies.
    '''
    class_: Literal['https://schema.org/DrugLegalStatus'] = Field( # type: ignore
        default='https://schema.org/DrugLegalStatus',
        alias='@type',
        serialization_alias='@type'
    )
    applicableLocation: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
