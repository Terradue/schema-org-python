from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.create_action import CreateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PaintAction(CreateAction):
    """
The act of producing a painting, typically with paint and canvas as instruments.
    """
    class_: Literal['https://schema.org/PaintAction'] = Field( # type: ignore
        default='https://schema.org/PaintAction',
        alias='@type',
        serialization_alias='@type'
    )
