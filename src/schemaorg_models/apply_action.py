from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organize_action import OrganizeAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ApplyAction(OrganizeAction):
    """
The act of registering to an organization/service without the guarantee to receive it.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """
    class_: Literal['https://schema.org/ApplyAction'] = Field( # type: ignore
        default='https://schema.org/ApplyAction',
        alias='@type',
        serialization_alias='@type'
    )
