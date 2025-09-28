from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.store import Store

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComputerStore(Store):
    """
A computer store.
    """
    class_: Literal['https://schema.org/ComputerStore'] = Field( # type: ignore
        default='https://schema.org/ComputerStore',
        alias='@type',
        serialization_alias='@type'
    )
