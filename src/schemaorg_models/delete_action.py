from typing import Literal
from pydantic import Field
from schemaorg_models.update_action import UpdateAction


class DeleteAction(UpdateAction):
    """
The act of editing a recipient by removing one of its objects.
    """
    class_: Literal['https://schema.org/DeleteAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
