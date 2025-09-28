from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.plan_action import PlanAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CancelAction(PlanAction):
    """
The act of asserting that a future event/action is no longer going to happen.\
\
Related actions:\
\
* [[ConfirmAction]]: The antonym of CancelAction.
    """
    class_: Literal['https://schema.org/CancelAction'] = Field( # type: ignore
        default='https://schema.org/CancelAction',
        alias='@type',
        serialization_alias='@type'
    )
