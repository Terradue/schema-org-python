from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Library(LocalBusiness):
    """
A library.
    """
    class_: Literal['https://schema.org/Library'] = Field( # type: ignore
        default='https://schema.org/Library',
        alias='@type',
        serialization_alias='@type'
    )
