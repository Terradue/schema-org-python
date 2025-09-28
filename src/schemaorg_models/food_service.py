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

class FoodService(Service):
    """
A food service, like breakfast, lunch, or dinner.
    """
    class_: Literal['https://schema.org/FoodService'] = Field( # type: ignore
        default='https://schema.org/FoodService',
        alias='@type',
        serialization_alias='@type'
    )
