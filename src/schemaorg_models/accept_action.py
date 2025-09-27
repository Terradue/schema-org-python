from typing import Literal
from pydantic import Field
from schemaorg_models.allocate_action import AllocateAction


class AcceptAction(AllocateAction):
    """
The act of committing to/adopting an object.\
\
Related actions:\
\
* [[RejectAction]]: The antonym of AcceptAction.
    """
    class_: Literal['https://schema.org/AcceptAction'] = Field(default='https://schema.org/AcceptAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
