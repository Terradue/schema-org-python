from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.physician import Physician

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PhysiciansOffice(Physician):
    """
A doctor's office or clinic.
    """
    class_: Literal['https://schema.org/PhysiciansOffice'] = Field( # type: ignore
        default='https://schema.org/PhysiciansOffice',
        alias='@type',
        serialization_alias='@type'
    )
