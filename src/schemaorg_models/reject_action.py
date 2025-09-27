from typing import Literal
from pydantic import Field
from schemaorg_models.allocate_action import AllocateAction


class RejectAction(AllocateAction):
    """
The act of rejecting to/adopting an object.\
\
Related actions:\
\
* [[AcceptAction]]: The antonym of RejectAction.
    """
    class_: Literal['https://schema.org/RejectAction'] = Field(default='https://schema.org/RejectAction', alias='class', serialization_alias='class') # type: ignore
