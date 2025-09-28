from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.add_action import AddAction

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.place import Place

class InsertAction(AddAction):
    """
The act of adding at a specific location in an ordered collection.
    """
    class_: Literal['https://schema.org/InsertAction'] = Field( # type: ignore
        default='https://schema.org/InsertAction',
        alias='@type',
        serialization_alias='@type'
    )
    toLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
