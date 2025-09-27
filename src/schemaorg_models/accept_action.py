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
    class_: Literal['https://schema.org/AcceptAction'] = Field(default='https://schema.org/AcceptAction', alias='class', serialization_alias='class') # type: ignore
