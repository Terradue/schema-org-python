from typing import Literal
from pydantic import Field
from schemaorg_models.assess_action import AssessAction


class IgnoreAction(AssessAction):
    """
The act of intentionally disregarding the object. An agent ignores an object.
    """
    class_: Literal['https://schema.org/IgnoreAction'] = Field(default='https://schema.org/IgnoreAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
