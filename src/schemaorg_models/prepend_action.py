from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.insert_action import InsertAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PrependAction(InsertAction):
    """
The act of inserting at the beginning if an ordered collection.
    """
    class_: Literal['https://schema.org/PrependAction'] = Field( # type: ignore
        default='https://schema.org/PrependAction',
        alias='@type',
        serialization_alias='@type'
    )
