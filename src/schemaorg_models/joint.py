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
from .anatomical_structure import AnatomicalStructure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_entity import MedicalEntity

class Joint(AnatomicalStructure):
    '''
    The anatomical location at which two or more bones make contact.

    Attributes:
        functionalClass: The degree of mobility the joint allows.
        structuralClass: The name given to how bone physically connects to each other.
        biomechnicalClass: The biomechanical properties of the bone.
    '''
    class_: Literal['https://schema.org/Joint'] = Field( # type: ignore
        default='https://schema.org/Joint',
        alias='@type',
        serialization_alias='@type'
    )
    functionalClass: Optional[Union['MedicalEntity', List['MedicalEntity'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'functionalClass',
            'https://schema.org/functionalClass'
        ),
        serialization_alias='https://schema.org/functionalClass'
    )
    structuralClass: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'structuralClass',
            'https://schema.org/structuralClass'
        ),
        serialization_alias='https://schema.org/structuralClass'
    )
    biomechnicalClass: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'biomechnicalClass',
            'https://schema.org/biomechnicalClass'
        ),
        serialization_alias='https://schema.org/biomechnicalClass'
    )
