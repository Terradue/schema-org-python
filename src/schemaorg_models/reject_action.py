from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.allocate_action import AllocateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RejectAction(AllocateAction):
    """
The act of rejecting to/adopting an object.\
\
Related actions:\
\
* [[AcceptAction]]: The antonym of RejectAction.
    """
    class_: Literal['https://schema.org/RejectAction'] = Field( # type: ignore
        default='https://schema.org/RejectAction',
        alias='@type',
        serialization_alias='@type'
    )
