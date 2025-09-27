from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.allocate_action import AllocateAction


class RejectAction(AllocateAction):
    """
The act of rejecting to/adopting an object.\
\
Related actions:\
\
* [[AcceptAction]]: The antonym of RejectAction.
    """
    type_: Literal['https://schema.org/RejectAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RejectAction'),serialization_alias='class') # type: ignore
