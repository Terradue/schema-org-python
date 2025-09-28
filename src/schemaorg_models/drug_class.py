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
from .drug import Drug

class DrugClass(MedicalEntity):
    """
A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.
    """
    class_: Literal['https://schema.org/DrugClass'] = Field( # type: ignore
        default='https://schema.org/DrugClass',
        alias='@type',
        serialization_alias='@type'
    )
    drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drug',
            'https://schema.org/drug'
        ),
        serialization_alias='https://schema.org/drug'
    )
