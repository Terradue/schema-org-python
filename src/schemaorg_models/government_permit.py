from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.permit import Permit

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GovernmentPermit(Permit):
    """
A permit issued by a government agency.
    """
    class_: Literal['https://schema.org/GovernmentPermit'] = Field( # type: ignore
        default='https://schema.org/GovernmentPermit',
        alias='@type',
        serialization_alias='@type'
    )
