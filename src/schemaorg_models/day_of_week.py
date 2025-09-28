from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DayOfWeek(Enumeration):
    """
The day of the week for which these opening hours are valid.
    """
    class_: Literal['https://schema.org/DayOfWeek'] = Field( # type: ignore
        default='https://schema.org/DayOfWeek',
        alias='@type',
        serialization_alias='@type'
    )
