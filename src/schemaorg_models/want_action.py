from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class WantAction(ReactAction):
    """
The act of expressing a desire about the object. An agent wants an object.
    """
    class_: Literal['https://schema.org/WantAction'] = Field(default='https://schema.org/WantAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
