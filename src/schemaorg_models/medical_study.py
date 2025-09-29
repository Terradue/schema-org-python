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
    from .event_status_type import EventStatusType
    from .person import Person
    from .administrative_area import AdministrativeArea
    from .medical_study_status import MedicalStudyStatus
    from .organization import Organization
    from .medical_condition import MedicalCondition

class MedicalStudy(MedicalEntity):
    '''
    A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.

    Attributes:
        studySubject: A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        status: The status of the study (enumerated).
        studyLocation: The location in which the study is taking/took place.
        healthCondition: Specifying the health condition(s) of a patient, medical study, or other target audience.
    '''
    class_: Literal['https://schema.org/MedicalStudy'] = Field( # type: ignore
        default='https://schema.org/MedicalStudy',
        alias='@type',
        serialization_alias='@type'
    )
    studySubject: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sponsor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
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
    studyLocation: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    healthCondition: Optional[Union['MedicalCondition', List['MedicalCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
