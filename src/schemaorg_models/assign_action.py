from typing import Literal
from pydantic import Field
from schemaorg_models.allocate_action import AllocateAction


class AssignAction(AllocateAction):
    """
The act of allocating an action/event/task to some destination (someone or something).
    """
    type_: Literal['https://schema.org/AssignAction'] = Field(default='https://schema.org/AssignAction', alias='@type', serialization_alias='@type') # type: ignore
