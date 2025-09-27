from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction


class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    type_: Literal['https://schema.org/MarryAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MarryAction'),serialization_alias='class') # type: ignore
