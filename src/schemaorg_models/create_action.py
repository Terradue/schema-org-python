from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CreateAction(Action):
    """
The act of deliberately creating/producing/generating/building a result out of the agent.
    """
    class_: Literal['https://schema.org/CreateAction'] = Field( # type: ignore
        default='https://schema.org/CreateAction',
        alias='@type',
        serialization_alias='@type'
    )
