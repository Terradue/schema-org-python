from typing import Literal
from pydantic import Field
from schemaorg_models.find_action import FindAction


class CheckAction(FindAction):
    """
An agent inspects, determines, investigates, inquires, or examines an object's accuracy, quality, condition, or state.
    """
    type_: Literal['https://schema.org/CheckAction'] = Field(default='https://schema.org/CheckAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
