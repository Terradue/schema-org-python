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

class FilmAction(CreateAction):
    """
The act of capturing sound and moving images on film, video, or digitally.
    """
    class_: Literal['https://schema.org/FilmAction'] = Field( # type: ignore
        default='https://schema.org/FilmAction',
        alias='@type',
        serialization_alias='@type'
    )
