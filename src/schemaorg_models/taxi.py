from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.service import Service

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Taxi(Service):
    """
A taxi.
    """
    class_: Literal['https://schema.org/Taxi'] = Field( # type: ignore
        default='https://schema.org/Taxi',
        alias='@type',
        serialization_alias='@type'
    )
