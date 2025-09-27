from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.allocate_action import AllocateAction


class AssignAction(AllocateAction):
    """
The act of allocating an action/event/task to some destination (someone or something).
    """
    type_: Literal['https://schema.org/AssignAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AssignAction'),serialization_alias='class') # type: ignore
