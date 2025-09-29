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
    from .medical_contraindication import MedicalContraindication

class MedicalDevice(MedicalEntity):
    '''
    Any object used in a medical capacity, such as to diagnose or treat a patient.

    Attributes:
        procedure: A description of the procedure involved in setting up, using, and/or installing the device.
        seriousAdverseOutcome: A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        adverseOutcome: A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
        preOp: A description of the workup, testing, and other preparations required before implanting this device.
        contraindication: A contraindication for this therapy.
        postOp: A description of the postoperative procedures, care, and/or followups for this device.
    '''
    class_: Literal['https://schema.org/MedicalDevice'] = Field( # type: ignore
        default='https://schema.org/MedicalDevice',
        alias='@type',
        serialization_alias='@type'
    )
    procedure: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'procedure',
            'https://schema.org/procedure'
        ),
        serialization_alias='https://schema.org/procedure'
    )
    seriousAdverseOutcome: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seriousAdverseOutcome',
            'https://schema.org/seriousAdverseOutcome'
        ),
        serialization_alias='https://schema.org/seriousAdverseOutcome'
    )
    adverseOutcome: Optional[Union['MedicalEntity', List['MedicalEntity']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'adverseOutcome',
            'https://schema.org/adverseOutcome'
        ),
        serialization_alias='https://schema.org/adverseOutcome'
    )
    preOp: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'preOp',
            'https://schema.org/preOp'
        ),
        serialization_alias='https://schema.org/preOp'
    )
    contraindication: Optional[Union[str, List[str], 'MedicalContraindication', List['MedicalContraindication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contraindication',
            'https://schema.org/contraindication'
        ),
        serialization_alias='https://schema.org/contraindication'
    )
    postOp: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postOp',
            'https://schema.org/postOp'
        ),
        serialization_alias='https://schema.org/postOp'
    )
