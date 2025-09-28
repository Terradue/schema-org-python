from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organization import Organization

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Cooperative(Organization):
    """
An organization that is a joint project of multiple organizations or persons.
    """
    class_: Literal['https://schema.org/Cooperative'] = Field( # type: ignore
        default='https://schema.org/Cooperative',
        alias='@type',
        serialization_alias='@type'
    )
