from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.update_action import UpdateAction


class DeleteAction(UpdateAction):
    """
The act of editing a recipient by removing one of its objects.
    """
    type_: Literal['https://schema.org/DeleteAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DeleteAction'),serialization_alias='class') # type: ignore
