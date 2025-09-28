from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.transfer_action import TransferAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TakeAction(TransferAction):
    """
The act of gaining ownership of an object from an origin. Reciprocal of GiveAction.\
\
Related actions:\
\
* [[GiveAction]]: The reciprocal of TakeAction.\
* [[ReceiveAction]]: Unlike ReceiveAction, TakeAction implies that ownership has been transferred.
    """
    class_: Literal['https://schema.org/TakeAction'] = Field( # type: ignore
        default='https://schema.org/TakeAction',
        alias='@type',
        serialization_alias='@type'
    )
