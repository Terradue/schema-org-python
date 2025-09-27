from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class DrinkAction(ConsumeAction):
    """
The act of swallowing liquids.
    """
    class_: Literal['https://schema.org/DrinkAction'] = Field(default='https://schema.org/DrinkAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
