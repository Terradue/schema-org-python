from typing import Literal
from pydantic import Field
from schemaorg_models.find_action import FindAction


class CheckAction(FindAction):
    """
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    """
    class_: Literal['https://schema.org/CheckAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
