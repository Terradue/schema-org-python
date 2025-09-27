from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ListenAction(ConsumeAction):
    """
The act of consuming audio content.
    """
    class_: Literal['https://schema.org/ListenAction'] = Field(default='https://schema.org/ListenAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
