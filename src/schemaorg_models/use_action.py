from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class UseAction(ConsumeAction):
    """
The act of applying an object to its intended purpose.
    """
    class_: Literal['https://schema.org/UseAction'] = Field(default='https://schema.org/UseAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
