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

class PhotographAction(CreateAction):
    """
The act of capturing still images of objects using a camera.
    """
    class_: Literal['https://schema.org/PhotographAction'] = Field( # type: ignore
        default='https://schema.org/PhotographAction',
        alias='@type',
        serialization_alias='@type'
    )
