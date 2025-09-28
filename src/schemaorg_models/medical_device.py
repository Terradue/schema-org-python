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
from .medical_contraindication import MedicalContraindication

class MedicalDevice(MedicalEntity):
    """
Any object used in a medical capacity, such as to diagnose or treat a patient.
    """
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
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seriousAdverseOutcome',
            'https://schema.org/seriousAdverseOutcome'
        ),
        serialization_alias='https://schema.org/seriousAdverseOutcome'
    )
    adverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
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
    contraindication: Optional[Union[str, List[str], MedicalContraindication, List[MedicalContraindication]]] = Field(
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
