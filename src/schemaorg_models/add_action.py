from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.update_action import UpdateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AddAction(UpdateAction):
    """
The act of editing by adding an object to a collection.
    """
    class_: Literal['https://schema.org/AddAction'] = Field( # type: ignore
        default='https://schema.org/AddAction',
        alias='@type',
        serialization_alias='@type'
    )
