from typing import Literal
from pydantic import Field
from schemaorg_models.update_action import UpdateAction


class DeleteAction(UpdateAction):
    """
The act of editing a recipient by removing one of its objects.
    """
    type_: Literal['https://schema.org/DeleteAction'] = Field(default='https://schema.org/DeleteAction', alias='@type', serialization_alias='@type') # type: ignore
