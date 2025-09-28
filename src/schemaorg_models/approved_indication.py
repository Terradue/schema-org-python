from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_indication import MedicalIndication

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
