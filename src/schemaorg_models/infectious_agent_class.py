from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_enumeration import MedicalEnumeration

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
