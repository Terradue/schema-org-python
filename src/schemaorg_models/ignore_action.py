from typing import Literal
from pydantic import Field
from schemaorg_models.assess_action import AssessAction


class IgnoreAction(AssessAction):
    """
The act of intentionally disregarding the object. An agent ignores an object.
    """
    type_: Literal['https://schema.org/IgnoreAction'] = Field(default='https://schema.org/IgnoreAction', alias='@type', serialization_alias='@type') # type: ignore
