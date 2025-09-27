from typing import Literal
from pydantic import Field
from schemaorg_models.interact_action import InteractAction


class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    class_: Literal['https://schema.org/MarryAction'] = Field(default='https://schema.org/MarryAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
