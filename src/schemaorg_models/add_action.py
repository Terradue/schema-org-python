from typing import Literal
from pydantic import Field
from schemaorg_models.update_action import UpdateAction


class AddAction(UpdateAction):
    """
The act of editing by adding an object to a collection.
    """
    class_: Literal['https://schema.org/AddAction'] = Field(default='https://schema.org/AddAction', alias='@type', serialization_alias='@type') # type: ignore
