from typing import Literal
from pydantic import Field
from schemaorg_models.interact_action import InteractAction


class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    class_: Literal['https://schema.org/MarryAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
