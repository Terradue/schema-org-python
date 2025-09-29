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
    from .medical_procedure_type import MedicalProcedureType
    from .event_status_type import EventStatusType
    from .medical_study_status import MedicalStudyStatus

class MedicalProcedure(MedicalEntity):
    '''
    A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.

    Attributes:
        bodyLocation: Location in the body of the anatomical structure.
        preparation: Typical preparation that a patient must undergo before having the procedure performed.
        status: The status of the study (enumerated).
        howPerformed: How the procedure is performed.
        procedureType: The type of procedure, for example Surgical, Noninvasive, or Percutaneous.
        followup: Typical or recommended followup care after the procedure is performed.
    '''
    class_: Literal['https://schema.org/MedicalProcedure'] = Field( # type: ignore
        default='https://schema.org/MedicalProcedure',
        alias='@type',
        serialization_alias='@type'
    )
    bodyLocation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    preparation: Optional[Union['MedicalEntity', List['MedicalEntity'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    status: Optional[Union['EventStatusType', List['EventStatusType'], 'MedicalStudyStatus', List['MedicalStudyStatus'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    howPerformed: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    procedureType: Optional[Union['MedicalProcedureType', List['MedicalProcedureType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    followup: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
