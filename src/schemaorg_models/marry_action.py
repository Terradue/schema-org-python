from typing import Literal
from pydantic import Field
from schemaorg_models.interact_action import InteractAction


class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    type_: Literal['https://schema.org/MarryAction'] = Field(default='https://schema.org/MarryAction', alias='@type', serialization_alias='@type') # type: ignore
