from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.interact_action import InteractAction


class UnRegisterAction(InteractAction):
    """
The act of un-registering from a service.\
\
Related actions:\
\
* [[RegisterAction]]: antonym of UnRegisterAction.\
* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.
    """
    type_: Literal['https://schema.org/UnRegisterAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/UnRegisterAction'),serialization_alias='class') # type: ignore
