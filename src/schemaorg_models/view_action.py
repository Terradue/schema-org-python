from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ViewAction(ConsumeAction):
    """
The act of consuming static visual content.
    """
    class_: Literal['https://schema.org/ViewAction'] = Field(default='https://schema.org/ViewAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
