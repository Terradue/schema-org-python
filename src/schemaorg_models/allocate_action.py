from typing import Literal
from pydantic import Field
from schemaorg_models.organize_action import OrganizeAction


class AllocateAction(OrganizeAction):
    """
The act of organizing tasks/objects/events by associating resources to it.
    """
    class_: Literal['https://schema.org/AllocateAction'] = Field(default='https://schema.org/AllocateAction', alias='class', serialization_alias='class') # type: ignore
