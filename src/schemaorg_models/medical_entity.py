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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_guideline import MedicalGuideline
    from .medical_enumeration import MedicalEnumeration
    from .organization import Organization
    from .medicine_system import MedicineSystem
    from .medical_specialty import MedicalSpecialty
    from .medical_code import MedicalCode
    from .drug_legal_status import DrugLegalStatus
    from .medical_study import MedicalStudy
    from .grant import Grant

class MedicalEntity(Thing):
    '''
    The most generic type of entity related to health and the practice of medicine.

    Attributes:
        code: A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
        guideline: A medical guideline related to this entity.
        legalStatus: The drug or supplement's legal status, including any controlled substance schedules that apply.
        recognizingAuthority: If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
        medicineSystem: The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        relevantSpecialty: If applicable, a medical specialty in which this entity is relevant.
        study: A medical study or trial related to this entity.
    '''
    class_: Literal['https://schema.org/MedicalEntity'] = Field( # type: ignore
        default='https://schema.org/MedicalEntity',
        alias='@type',
        serialization_alias='@type'
    )
    code: Optional[Union['MedicalCode', List['MedicalCode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    guideline: Optional[Union['MedicalGuideline', List['MedicalGuideline']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    legalStatus: Optional[Union['DrugLegalStatus', List['DrugLegalStatus'], 'MedicalEnumeration', List['MedicalEnumeration'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    recognizingAuthority: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    medicineSystem: Optional[Union['MedicineSystem', List['MedicineSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relevantSpecialty: Optional[Union['MedicalSpecialty', List['MedicalSpecialty']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    study: Optional[Union['MedicalStudy', List['MedicalStudy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
