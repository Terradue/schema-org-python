from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

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

class TransferAction(Action):
    """
The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.
    """
    class_: Literal['https://schema.org/TransferAction'] = Field( # type: ignore
        default='https://schema.org/TransferAction',
        alias='@type',
        serialization_alias='@type'
    )
    fromLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fromLocation',
            'https://schema.org/fromLocation'
        ),
        serialization_alias='https://schema.org/fromLocation'
    )
    toLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
