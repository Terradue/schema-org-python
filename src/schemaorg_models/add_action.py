from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.update_action import UpdateAction


class AddAction(UpdateAction):
    """
The act of editing by adding an object to a collection.
    """
    type_: Literal['https://schema.org/AddAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AddAction'),serialization_alias='class') # type: ignore
