from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ReadAction(ConsumeAction):
    """
The act of consuming written content.
    """
    type_: Literal['https://schema.org/ReadAction'] = Field(default='https://schema.org/ReadAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
