from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.allocate_action import AllocateAction


class AcceptAction(AllocateAction):
    """
The act of committing to/adopting an object.\
\
Related actions:\
\
* [[RejectAction]]: The antonym of AcceptAction.
    """
    type_: Literal['https://schema.org/AcceptAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AcceptAction'),serialization_alias='class') # type: ignore
