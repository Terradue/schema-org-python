from typing import Literal
from pydantic import Field
from schemaorg_models.allocate_action import AllocateAction


class AssignAction(AllocateAction):
    """
The act of allocating an action/event/task to some destination (someone or something).
    """
    class_: Literal['https://schema.org/AssignAction'] = Field(default='https://schema.org/AssignAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
