from typing import Literal
from pydantic import Field
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
    class_: Literal['https://schema.org/UnRegisterAction'] = Field(default='https://schema.org/UnRegisterAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
