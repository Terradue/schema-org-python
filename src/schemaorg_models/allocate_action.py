from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organize_action import OrganizeAction


class AllocateAction(OrganizeAction):
    """
The act of organizing tasks/objects/events by associating resources to it.
    """
    type_: Literal['https://schema.org/AllocateAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AllocateAction'),serialization_alias='class') # type: ignore
