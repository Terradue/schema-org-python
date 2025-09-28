from __future__ import annotations

from .medical_enumeration import MedicalEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InfectiousAgentClass(MedicalEnumeration):
    """
Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """
    class_: Literal['https://schema.org/InfectiousAgentClass'] = Field( # type: ignore
        default='https://schema.org/InfectiousAgentClass',
        alias='@type',
        serialization_alias='@type'
    )
