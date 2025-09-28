from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.automotive_business import AutomotiveBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    class_: Literal['https://schema.org/AutoWash'] = Field( # type: ignore
        default='https://schema.org/AutoWash',
        alias='@type',
        serialization_alias='@type'
    )
