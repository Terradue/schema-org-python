from typing import Literal
from pydantic import Field
from schemaorg_models.allocate_action import AllocateAction


class AssignAction(AllocateAction):
    """
The act of allocating an action/event/task to some destination (someone or something).
    """
    class_: Literal['https://schema.org/AssignAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
