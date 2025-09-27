from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class EatAction(ConsumeAction):
    """
The act of swallowing solid objects.
    """
    class_: Literal['https://schema.org/EatAction'] = Field(default='https://schema.org/EatAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
