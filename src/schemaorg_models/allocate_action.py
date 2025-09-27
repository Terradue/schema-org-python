from typing import Literal
from pydantic import Field
from schemaorg_models.organize_action import OrganizeAction


class AllocateAction(OrganizeAction):
    """
The act of organizing tasks/objects/events by associating resources to it.
    """
    class_: Literal['https://schema.org/AllocateAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
