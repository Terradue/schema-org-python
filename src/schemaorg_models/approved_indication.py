from __future__ import annotations

from .medical_indication import MedicalIndication    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ApprovedIndication(MedicalIndication):
    """
An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.
    """
    class_: Literal['https://schema.org/ApprovedIndication'] = Field( # type: ignore
        default='https://schema.org/ApprovedIndication',
        alias='@type',
        serialization_alias='@type'
    )
