from typing import Literal
from pydantic import Field
from schemaorg_models.assess_action import AssessAction


class ReactAction(AssessAction):
    """
The act of responding instinctively and emotionally to an object, expressing a sentiment.
    """
    class_: Literal['https://schema.org/ReactAction'] = Field(default='https://schema.org/ReactAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
